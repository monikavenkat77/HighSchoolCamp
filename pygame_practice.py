"""
title: pygame_practice
author: Monika
date: 2019-06-14 09:50
"""

# Import a library of functions called 'pygame'
import pygame

# Initialize the game engine
pygame.init()

# Set the height and width of the screen
size = (500, 700)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("First Pygame")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# Loop as long as done == False
while not done:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    BROWN = (205,133,63)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    pi = 3.14159

    screen.fill(WHITE)

    pygame.draw.polygon(screen, BLACK, [[7, 200], [50, 18], [170, 18], [207.5, 200]], )
    pygame.draw.circle(screen, BROWN, [110,110], 75)
    pygame.draw.arc(screen, RED, [55, 60, 110, 110], pi, (5*pi)/3, 3)
    pygame.draw.polygon(screen, BLACK, [[70, 75], [80,60], [90, 75]],)
    pygame.draw.polygon(screen, BLACK, [[125, 75], [135, 60], [145, 75]], )
    pygame.draw.line(screen, BROWN, [107.5, 175], [107.5, 450], 7)


    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

# Be IDLE friendly
pygame.quit()