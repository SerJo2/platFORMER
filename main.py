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
player_v_momentum = 0

player_rect = pygame.Rect(cords[0], cords[1], player_image.get_width(), player_image.get_height())
test_rect = pygame.Rect(100, 100, 50, 100)
while True:
    screen.fill((146, 244, 255))
    screen.blit(player_image, cords)

    if mov_left:
        cords[0] -= 4
    if mov_right:
        cords[0] += 4

    if cords[1] > WINDOW_SIZE[1] - player_image.get_height():
        player_v_momentum = -player_v_momentum
        pass
    else:
        player_v_momentum += 0.2
    cords[1] += player_v_momentum

    player_rect.x = cords[0]
    player_rect.y = cords[1]

    if player_rect.colliderect(test_rect):
        pygame.draw.rect(screen, (255, 0, 0), test_rect)
    else:
        pygame.draw.rect(screen, (0, 0, 0), test_rect)

    for event in pygame.event.get():
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
