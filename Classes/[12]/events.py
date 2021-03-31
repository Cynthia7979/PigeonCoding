import pygame
import sys
from pygame.locals import *


def main():
    WIDTH, HEIGHT = 1000, 600
    XSTEP = 10
    YSTEP = 10
    xspeed = 0
    yspeed = 0

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
        ball_rect.x += xspeed
        ball_rect.y += yspeed
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    xspeed = XSTEP
                elif event.key == pygame.K_LEFT:
                    xspeed = -XSTEP
                elif event.key == pygame.K_UP:
                    yspeed = -YSTEP
                elif event.key == pygame.K_DOWN:
                    yspeed = YSTEP
            elif event.type == KEYUP:
                if event.key == pygame.K_q:
                    terminate()
                elif event.key in (pygame.K_RIGHT, pygame.K_LEFT):
                    xspeed = 0
                elif event.key in (pygame.K_UP, pygame.K_DOWN):
                    yspeed = 0

        pygame.display.flip()
        clock.tick(30)


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
