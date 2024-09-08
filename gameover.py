import pygame
from constants import *

# Function to handle game over screen
def game_over_screen(screen):
    
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)
    
    screen.fill("black")
    game_over_text = font.render("Game Over", True, "white")
    retry_text = small_font.render("Press 'R' to Retry or 'Q' to Quit", True, "white")

    screen.blit(game_over_text, (SCREEN_WIDTH / 2 - 200, SCREEN_HEIGHT/3))
    screen.blit(retry_text, (SCREEN_WIDTH / 2 - 200, SCREEN_HEIGHT/2))
    pygame.display.flip()

# Function to restart the game
def restart_game():
    pass