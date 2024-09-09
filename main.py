import time
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from gameover import game_over_screen, restart_game

def main():
    
    #Initialise the game
    pygame.init()
    print("Starting asteroids!")

    #setting the window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #setting fonts
    font = pygame.font.Font('PressStart2P-Regular.ttf', 74)
    small_font = pygame.font.Font('PressStart2P-Regular.ttf', 30)
    
    #Game groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #Add game objects to the groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    #Create a player and spawn it to the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    
    #Create asteroid field
    asteroidField = AsteroidField()
    
    #Game Clock
    clock = pygame.time.Clock() 
    dt = 0  #delta to store time since last frame in seconds

    ### GAME LOOP ###
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        ###Background###
        image = pygame.image.load('space_darker.jpg')
        # Resize the image to fit the screen
        image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        # Fill the screen with the image
        screen.blit(image, (0, 0))
        
        #Update game objects
        for obj in updatable:
            obj.update(dt)
        
        #Game mechanics
        for asteroid in asteroids:
            if asteroid.is_collided(player):
                
                #Loosing lifes
                player.num_lifes -= 1
                print(f"You died. {player.num_lifes} life out of {PLAYER_NUM_LIFES} left")
                player.position = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                
                #Game over:
                if player.num_lifes == 0:
                    
                    #Record Player's score to file
                    print(f"Your score is {player.score}!")
                    with open('scores.txt', 'a') as file:
                        file.write(f"Player score is {player.score}\n")
                        print("Your score is recored in scores.txt")
                    
                    #Gameover and retry calls
                    game_over_screen(screen)
                    time.sleep(1)
                    sys.exit()
                    """
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_r]:
                        restart_game()
                    if keys[pygame.K_q]:
                        sys.exit()
                    """
            #Shooting
            for shot in shots:
                if asteroid.is_collided(shot): 
                    asteroid.split()
                    shot.kill()
                    player.score += 100 // asteroid.radius
        
        # Draw all drawable objects to the game screen
        for obj in drawable:
            obj.draw(screen) 
        
        # Draw player lives on the screen
        lives_text = small_font.render(f"Lives: {player.num_lifes}", True, "white")
        screen.blit(lives_text, (10, 10))

        # Draw player's score on the screen
        score_text = small_font.render(f"Score: {player.score}", True, "white")
        screen.blit(score_text, (10, 50))

        #Update the display
        pygame.display.flip()
        
        #Game Timer. Limit frame rate to 60 FPS and store time since last frame in dt in seconds
        dt = clock.tick(60)/1000 

if __name__ == "__main__":
    main()
