import pygame
from constants import *
from player import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # The center of the screen:
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    #create a player
    player = Player(x, y, PLAYER_RADIUS)

    #setting the window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #RGB colours
    red = (255, 0, 0)
    black = (0, 0, 0)

    
    clock = pygame.time.Clock() #clock to limit FPS
    dt = 0  #delta time since last frame in seconds

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(black) # fill the screen with black
        player.update(dt)
        player.draw(screen) # render player on the scrren
        pygame.display.flip()
        dt = clock.tick(60)/1000 #limit FPS to 60 and store time since last frame in dt in seconds

if __name__ == "__main__":
    main()


######I don't know why VS code doesn't pick up pygame module###