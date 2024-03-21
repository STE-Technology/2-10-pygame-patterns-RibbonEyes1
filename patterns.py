"""
File: patterns.py
Author: Your Name
Date: 2024-03-21
Description: Template for basic Pygame graphics setup.
"""

import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Patterns")

# Define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN=(27, 135, 85)
PURPLE=(116, 93, 156)
# Main loop
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw graphics
    # --(start here)---------------------------------------------------------
    screen.fill(WHITE)
    pygame.draw.circle(screen,GREEN,(730,90),20)
    pygame.draw.circle(screen,GREEN,(650,90),20)
    pygame.draw.circle(screen,GREEN,(570,90),20)
    pygame.draw.circle(screen,GREEN,(490,90),20)
    pygame.draw.circle(screen,GREEN,(730,170),20)
    pygame.draw.circle(screen,GREEN,(650,170),20)
    pygame.draw.circle(screen,GREEN,(570,170),20)
    pygame.draw.circle(screen,GREEN,(490,170),20)
    pygame.draw.circle(screen,GREEN,(730,250),20)
    pygame.draw.circle(screen,GREEN,(650,250),20)
    pygame.draw.circle(screen,GREEN,(570,250),20)
    pygame.draw.circle(screen,GREEN,(490,250),20)
    pygame.draw.circle(screen,GREEN,(730,330),20)
    pygame.draw.circle(screen,GREEN,(650,330),20)
    pygame.draw.circle(screen,GREEN,(570,330),20)
    pygame.draw.circle(screen,GREEN,(490,330),20)

    pygame.draw.line(screen,PURPLE,)


    # --(leave below)--------------------------------------------------------

    # Update display
    pygame.display.flip()

# Quit Pygame   
pygame.quit()
sys.exit()
