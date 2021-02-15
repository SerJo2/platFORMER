import pygame
import sys
from pygame.locals import *

clock = pygame.time.Clock()
pygame.init()

WINDOW_SIZE = (600, 400)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

disp = pygame.Surface((300, 200))

pygame.display.set_caption('platFORMER')

player_image = pygame.image.load('player.png')
player_image.set_colorkey('white')
dirt_image = pygame.image.load('dirt.png')
grass_image = pygame.image.load('grass.png')

# game_map[y][x]

game_map = [['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '2', '2', '2', '2', '2', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['2', '2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '2', '2'],
            ['1', '1', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']]


def collide_test(rect, tiles):
    pass

mov_right = False
mov_left = False
cords = [50, 50]
player_v_momentum = 0

player_rect = pygame.Rect(cords[0], cords[1], player_image.get_width(), player_image.get_height())

while True:
    disp.fill((146, 244, 255))


    tile_rects = []
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            if tile == '1':
                disp.blit(dirt_image, (x * 16, y * 16))
            if tile == '2':
                disp.blit(grass_image, (x * 16, y * 16))
            if tile != '0':
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))
            x += 1
        y += 1

    disp.blit(player_image, cords)
    if mov_left:
        cords[0] -= 4
    if mov_right:
        cords[0] += 4

    player_v_momentum += 0.2
    cords[1] += player_v_momentum

    player_rect.x = cords[0]
    player_rect.y = cords[1]

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

    surf = pygame.transform.scale(disp, WINDOW_SIZE)

    screen.blit(surf, (0, 0))
    pygame.display.update()
    clock.tick(60)
