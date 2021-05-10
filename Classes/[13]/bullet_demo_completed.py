import pygame
import sys
from pygame.locals import *


WIDTH, HEIGHT = 1000, 800
bullet_img = pygame.surface.Surface((10, 10))
bullet_img.fill('yellow')
FPS = 30


class Bullet:
    def __init__(self, speed_x, speed_y):
        self.rect = pygame.rect.Rect((0, 0), bullet_img.get_size())
        self.rect.center = (0, HEIGHT/2)
        self.speed_x, self.speed_y = speed_x, speed_y

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def draw(self, surf):
        surf.blit(bullet_img, self.rect)
        return surf

    def collided_with(self, rect):
        return self.rect.colliderect(rect)


def main():
    pygame.init()
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    bullets = []
    obstruct_surf = pygame.surface.Surface((50, 50))
    obstruct_surf.fill('black')
    obstruct_rect = pygame.rect.Rect((800, HEIGHT/2), (50, 50))

    while True:  # main loop
        display.fill((255, 255, 255))
        display.blit(obstruct_surf, obstruct_rect)
        # print(bullets)
        for i in range(len(bullets)-1, -1, -1):
            print('processing bullet', i)
            bullet = bullets[i]
            bullet.move()
            if bullet.collided_with(obstruct_rect):
                bullets.pop(i)
            else:
                display = bullet.draw(display)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                if event.key == K_SPACE:
                    bullets.append(Bullet(20, 0))
                    print('Bullet added')
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
