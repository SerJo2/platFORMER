import pygame
import sys
from pygame.locals import *


clock = pygame.time.Clock()
pygame.init()

WINDOW_SIZE = (400, 400)


screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
pygame.display.set_caption('platFORMER')

player_image = pygame.image.load('player.png')

mov_right = False
mov_left = False
cords = [50, 50]

while True:
    
    for event in pygame.event.get():
        screen.fill((146,244,255))

        if mov_left:
            cords[0] -= 4
        if mov_right:
            cords[0] += 4
        screen.blit(player_image, cords)

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                mov_right = True
            if event.key == K_LEFT:
                mov_left = True
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                mov_right = False
            if event.key == K_LEFT:
                mov_left = False




    pygame.display.update()
    clock.tick(60)
