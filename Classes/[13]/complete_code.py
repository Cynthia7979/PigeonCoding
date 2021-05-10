import pygame
import sys
import random
from pygame.locals import *

WIDTH, HEIGHT = 1000, 800
bullet_img = pygame.surface.Surface((10, 10))
bullet_img.fill('yellow')
enemy_img = pygame.surface.Surface((20, 60))
enemy_img.fill('red')
FPS = 30


class Sprite:
    def __init__(self, image, speed_x, speed_y):
        self.rect = pygame.rect.Rect((0, 0), image.get_size())
        self.speed_x, self.speed_y = speed_x, speed_y
        self.image = image

    def move(self, *args):
        pass  # 每个子类的实现都不一样

    def draw(self, surf):
        surf.blit(self.image, self.rect)
        return surf

    def collided_with(self, rect):
        return self.rect.colliderect(rect)


class Bullet(Sprite):
    def __init__(self, speed_x, speed_y):
        super().__init__(bullet_img, speed_x, speed_y)
        self.rect = pygame.rect.Rect((0, 0), bullet_img.get_size())
        self.rect.center = (0, HEIGHT/2)
        self.speed_x, self.speed_y = speed_x, speed_y

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y


class Enemy:
    def __init__(self, image, speed_x, speed_y):
        # Get random spawn point
        x, y = random.randint(0, 1) * random.randint(0, WIDTH), random.randint(0, 1) * random.randint(HEIGHT)
        self.rect = pygame.rect.Rect((x, y), enemy_img.get_size())
        self.speed_x, self.speed_y = 5, 5

    def move(self, player_pos):
        if player_pos[0] > self.rect.x:
            self.rect.x += self.speed_x
        elif player_pos[0] < self.rect.x:
            self.rect.x -= self.speed_x
        if player_pos[1] > self.rect.y:
            self.rect.y += self.speed_y
        elif player_pos[1] < self.rect.y:
            self.rect.y -= self.speed_y

    def draw(self, surf):
        surf.blit(enemy_img, self.rect)
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
