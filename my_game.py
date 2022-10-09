import pygame
from pygame.locals import*
pygame.init()

import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

fpsClock = pygame.time.Clock()
fps = 60

width, height = 640, 480
screen = pygame.display.set_mode((width, height))

while True:
    scren.fill((0,0,0))
    
    for event i pygame event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    fpsClock.tick(fps)
