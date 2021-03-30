import pygame
import sys
from pygame.locals import *


def main():
    WIDTH, HEIGHT = 1000, 600
    XSPEED = 10
    YSPEED = 10

    pygame.init()
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    ball_surf = pygame.image.load('ball.png')
    ball_surf = pygame.transform.scale(ball_surf, (50, 50))
    ball_rect = ball_surf.get_rect()
    ball_rect.midleft = (0, HEIGHT/2)

    while True:  # main loop
        display.fill((255, 255, 255))
        display.blit(ball_surf, ball_rect)
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYUP:
                if event.key == pygame.K_q:
                    terminate()
                elif event.key == pygame.K_RIGHT:
                    ball_rect.x += XSPEED
                elif event.key == pygame.K_LEFT:
                    ball_rect.x -= XSPEED
                elif event.key == pygame.K_UP:
                    ball_rect.y -= YSPEED
                elif event.key == pygame.K_DOWN:
                    ball_rect.y += YSPEED

        pygame.display.flip()
        clock.tick(30)


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
