import pygame
import sys

# Function to prompt for user input
def prompt_user_input(screen, prompt_text="Enter your input:", font = None):
    # Create the font inside the function if not provided
    if font is None:
        font = pygame.font.Font(None, 48)  # Default font with size 48

    input_active = True
    user_input = ""
    prompt_surface = font.render(prompt_text, True, (255, 255, 255))  # Render prompt text
    
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # When 'Enter' is pressed, stop input
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:  # Handle backspace
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode  # Add the typed character to the input string

        # Clear the screen
        screen.fill((0, 0, 0))

        # Render the input text
        input_surface = font.render(user_input, True, (255, 255, 255))  # Render user input

        # Display the prompt and input text
        screen.blit(prompt_surface, (20, 50))  # Display prompt text at (20, 50)
        screen.blit(input_surface, (20, 150))  # Display input text at (20, 150)

        # Refresh the screen
        pygame.display.flip()

    return user_input