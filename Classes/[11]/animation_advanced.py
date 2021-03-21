import pygame
import sys
from pygame.locals import *

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
    ball_rect.x += XSPEED
    ball_rect.y += YSPEED
    if ball_rect.right >= WIDTH or ball_rect.left < 0:
        ball_rect.x -= 2*XSPEED
        XSPEED = -XSPEED
    if ball_rect.bottom >= HEIGHT or ball_rect.top < 0:
        ball_rect.y -= 2*YSPEED
        YSPEED = -YSPEED
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    clock.tick(30)
