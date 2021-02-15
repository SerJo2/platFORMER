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
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list


def move(rect, movement, tiles):
    collide_type = {'top': False, 'bottom': False, 'right': False, 'left': False}
    rect.x += movement[0]
    hit_list = collide_test(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collide_type['right'] = True
        if movement[0] < 0:
            rect.left = tile.right
            collide_type['left'] = True

    rect.y += movement[1]
    hit_list = collide_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collide_type['bottom'] = True
        if movement[1] < 0:
            rect.top = tile.bottom
            collide_type['top'] = True

    return rect, collide_type


mov_right = False
mov_left = False
air_timer = 0
cords = [50, 50]
player_v_momentum = 0
how_jmp = 2

player_rect = pygame.Rect(cords[0], cords[1], player_image.get_width(), player_image.get_height())
player_movement = [0, 0]

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

    player_movement = [0, 0]
    if mov_right:
        player_movement[0] += 2
    if mov_left:
        player_movement[0] -= 2
    player_movement[1] += player_v_momentum
    player_v_momentum += 0.2
    if player_v_momentum > 3:
        player_v_momentum = 3
    player_rect, collisions = move(player_rect, player_movement, tile_rects)

    if collisions['bottom']:
        player_v_momentum = 1
        air_timer = 0
        how_jmp = 2
    else:
        air_timer += 1

    if collisions['top']:
        player_v_momentum = 0

    disp.blit(player_image, (player_rect.x, player_rect.y))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                mov_right = True
            if event.key == K_LEFT:
                mov_left = True
            if event.key == K_UP:
                if air_timer < 5 and how_jmp == 2:
                    player_v_momentum = -3
                    how_jmp -= 1
                elif (how_jmp == 1 or how_jmp == 2) and air_timer >= 5:
                    player_v_momentum = -3
                    how_jmp = 0
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                mov_right = False
            if event.key == K_LEFT:
                mov_left = False

    surf = pygame.transform.scale(disp, WINDOW_SIZE)

    screen.blit(surf, (0, 0))
    pygame.display.update()
    clock.tick(60)
