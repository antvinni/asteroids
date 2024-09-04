import pygame

from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
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
        screen.fill(black)
        pygame.display.flip()
        dt = clock.tick(60)/1000 #limit FPS to 60 and store time since last frame in dt in seconds

if __name__ == "__main__":
    main()