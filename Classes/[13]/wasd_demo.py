import pygame
import sys
from pygame.locals import *


WIDTH, HEIGHT = 1000, 800
FPS = 300


def main():
    pygame.init()
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    player_moving_x = 0
    player_moving_y = 0
    player_speed = 5
    player_surf = pygame.surface.Surface((10, 10))
    player_surf.fill('blue')
    player_rect = player_surf.get_rect()
    player_rect.topleft = (0, 0)

    while True:  # main loop
        display.fill((255, 255, 255))

        player_rect.x += player_moving_x
        player_rect.y += player_moving_y
        display.blit(player_surf, player_rect)

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYUP:
                if event.key in (K_w, K_s):
                    player_moving_y = 0
                elif event.key in (K_a, K_d):
                    player_moving_x = 0
            elif event.type == KEYDOWN:
                if event.key == K_w:
                    player_moving_y = -player_speed
                elif event.key == K_s:
                    player_moving_y = player_speed
                elif event.key == K_a:
                    player_moving_x = -player_speed
                elif event.key == K_d:
                    player_moving_x = player_speed
        pygame.display.flip()
        clock.tick(FPS)


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
