import pygame
import sys
from pygame.locals import *

pygame.init()
display = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()
ball_surf = pygame.image.load('ball.png')
ball_surf = pygame.transform.scale(ball_surf, (50, 50))
ball_rect = ball_surf.get_rect()
ball_rect.midleft = (0, 300)

while True:  # main loop
    display.fill((255, 255, 255))
    display.blit(ball_surf, ball_rect)
    ball_rect.left += 30
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    clock.tick(30)
