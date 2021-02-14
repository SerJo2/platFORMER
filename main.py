import pygame
import sys
from pygame.locals import *


clock = pygame.time.Clock()
pygame.init()

WINDOW_SIZE = (400, 400)


screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
pygame.display.set_caption('platFORMER')

player_image = pygame.image.load('player.png')

while True:
    
    for event in pygame.event.get():

        screen.blit(player_image, (50, 50))

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)