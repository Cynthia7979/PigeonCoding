import pygame
import sys
from pygame.locals import *


WIDTH, HEIGHT = 1000, 800
bullet_img = pygame.surface.Surface((10, 10))
bullet_img.fill('yellow')
FPS = 60


class Bullet:
    def __init__(self, speed_x, speed_y):
        self.rect = pygame.rect.Rect((0, 0), bullet_img.get_size())
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.speed_x, self.speed_y = speed_x, speed_y

    def move(self):
        pass  # 移动到下一帧的位置

    def draw(self, surf):
        pass  # 将子弹的图像绘制到图层上

    def collided_with(self, rect):
        pass  # 如果self.rect和rect碰撞，则返回True，反之返回False
        # 碰撞检测函数：Rect.colliderect(rect)


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
        for i in range(0, len(bullets), -1):
            print('processing bullet', i)
            bullet = bullets[i]
            bullet.move()
            if bullet.collided_with(obstruct_rect):
                bullets.pop(i)
            else:
                bullet.draw(display)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                if event.key == K_SPACE:
                    bullets.append(Bullet(20, 0))
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
