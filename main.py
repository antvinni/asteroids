import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    
    #Initialise the game
    pygame.init()
    print("Starting asteroids!")

    #setting the window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
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
        
        #Screen background
        screen.fill('black') 
        
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
                    print(f"Your score is {player.score}!")
                    with open('scores.txt', 'a') as file:
                        file.write(f"Player score is {player.score}\n")
                        print("Your score is recored in scores.txt")
                    print("Game over!")
                    sys.exit()
            
            #Shooting
            for shot in shots:
                if asteroid.is_collided(shot): 
                    asteroid.split()
                    shot.kill()
                    player.score += 10
        
        for obj in drawable:
            obj.draw(screen) # render drawable on the scrren
        
        #Update the display
        pygame.display.flip()
        
        #Game Timer. Limit frame rate to 60 FPS and store time since last frame in dt in seconds
        dt = clock.tick(60)/1000 

if __name__ == "__main__":
    main()
