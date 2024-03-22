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
RED=(255,3,66)
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

    for circle in range(490,801,80):
        pygame.draw.circle(screen,GREEN,(circle,80),20)
        pygame.draw.circle(screen,GREEN,(circle,170),20)
        pygame.draw.circle(screen,GREEN,(circle,260),20)
        pygame.draw.circle(screen,GREEN,(circle,350),20)

    for vertical in range(10,401,40):
        pygame.draw.line(screen,PURPLE,(400,vertical),(10,vertical),width=2)

    for horizon in range(10,401,40):
        pygame.draw.line(screen,PURPLE,(horizon,375),(horizon,5),width=2)

  
    pygame.draw.line(screen,(255,0,4),(10,400),(450,140),width=40) 

    # --(leave below)--------------------------------------------------------

    # Update display
    pygame.display.flip()

# Quit Pygame   
pygame.quit()
sys.exit()
