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
size = (600, 800)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("First Pygame")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# Loop as long as done == False

BROWN = (205, 133, 63)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pi = 3.14159

x_speed = 0
y_speed = 0

x_coord = 10
y_coord = 10

ball_pos = 0
ball_change = 1

def draw_stick_figure(screen, x, y):
    pygame.draw.ellipse(screen, GREEN, [20 + x, 200 + ball_pos + y, 40, 40])
    pygame.draw.polygon(screen, BLACK, [[6 + x, 225 + y], [50 + x, 20 + y], [170 + x, 20 + y], [208.5 + x, 225 + y]], )
    pygame.draw.circle(screen, BROWN, [110 + x, 110 + y], 75)
    pygame.draw.arc(screen, RED, [55 + x, 60 + y, 110, 110], pi, (5*pi)/3, 3)
    pygame.draw.polygon(screen, BLACK, [[70 + x,80 + y], [80 + x,60 + y], [90 + x, 80 + y]],)
    pygame.draw.polygon(screen, BLACK, [[125 + x, 80 + y], [135 + x, 60 + y], [145 + x, 80 + y]], )
    pygame.draw.line(screen, BROWN, [107.5 + x, 175 + y], [107.5 + x, 400 + y], 7)
    pygame.draw.line(screen, BROWN, [107.5 + x, 200 + y], [40 + x, 225 + y], 7)
    pygame.draw.line(screen, BROWN, [107.5 + x, 200 + y], [135 + x, 300 + y], 7)
    pygame.draw.line(screen, BROWN, [107.5 + x, 400 + y], [80 + x, 500 + y], 7)
    pygame.draw.line(screen, BROWN, [107.5 + x, 400 + y], [135 + x, 500 + y], 7)

while not done:
    ball_pos += ball_change
    if ball_pos > 275:
        ball_change -= 1
    elif ball_pos < 100:
        ball_change += 1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x_speed = -3
    if keys[pygame.K_RIGHT]:
        x_speed = 3
    if keys[pygame.K_UP]:
        y_speed = -3
    if keys[pygame.K_DOWN]:
        y_speed = 3

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    x_coord += x_speed
    y_coord += y_speed

    x_speed = 0
    y_speed = 0

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    screen.fill(WHITE)

    draw_stick_figure(screen, x_coord, y_coord)

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

# Be IDLE friendly
pygame.quit()