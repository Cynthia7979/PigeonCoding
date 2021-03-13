import pygame
import sys
from pygame.locals import * 

pygame.init()
display = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()
font = pygame.font.Font('times.ttf', 72)
text_surf = font.render('Hello World!', True, (0,0,0), (255, 255, 255))
text_rect = text_surf.get_rect()
text_rect.topleft = (100, 100)

while True:  # main loop
    display.fill((255, 255, 255))
    display.blit(text_surf, text_rect)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    clock.tick(30)