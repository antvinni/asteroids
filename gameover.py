import pygame
import sys
from constants import *

# Function to handle game over screen
def game_over_screen(screen):
    
    font = pygame.font.Font('PressStart2P-Regular.ttf', 74)
    small_font = pygame.font.Font('PressStart2P-Regular.ttf', 30)
    
    ###Background###
    image = pygame.image.load('space.jpg')
    # Resize the image to fit the screen
    image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    # Fill the screen with the image
    screen.blit(image, (0, 0))
    
    game_over_text = font.render("Game Over", True, "white")
    retry_text = small_font.render("Press 'R' to Retry", True, "white")
    quit_text = small_font.render("Or any other key to Quit", True, "white")

    screen.blit(game_over_text, (SCREEN_WIDTH / 2 - 350, SCREEN_HEIGHT/3))
    screen.blit(retry_text, (SCREEN_WIDTH / 2 - 350, SCREEN_HEIGHT/2))
    screen.blit(quit_text, (SCREEN_WIDTH / 2 - 350, SCREEN_HEIGHT/1.6))
    pygame.display.flip()


    