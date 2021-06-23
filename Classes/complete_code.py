import pygame
import sys
import random
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 1000, 800
BULLET_SPEED = 20
PLAYER_SPEED = 5
ENEMY_SPEED = 7
BULLET_IMG = pygame.surface.Surface((10, 10))
BULLET_IMG.fill('yellow')
ENEMY_IMG = pygame.surface.Surface((20, 20))
ENEMY_IMG.fill('darkred')
PLAYER_IMG = pygame.surface.Surface((30, 30))
PLAYER_IMG.fill('blue')
FONT = pygame.font.SysFont('Arial', 32, True)
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

    def collided_with(self, other):
        try:
            return self.rect.colliderect(other)
        except AttributeError:
            return self.rect.colliderect(other.rect)


class Bullet(Sprite):
    def __init__(self, speed_x, speed_y, pos):
        super().__init__(BULLET_IMG, speed_x, speed_y)
        self.rect = pygame.rect.Rect((0, 0), BULLET_IMG.get_size())
        self.rect.center = pos
        self.speed_x, self.speed_y = speed_x, speed_y

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y


class Enemy(Sprite):
    def __init__(self, image, speed_x=5, speed_y=5):
        super().__init__(image, speed_x, speed_y)
        # Get random spawn point
        vertical_borders = random.randint(0,1)
        if vertical_borders:
            x, y = random.randint(0, WIDTH), random.randint(0, 1) * HEIGHT
        else:
            x, y = random.randint(0, 1) * WIDTH, random.randint(0, HEIGHT)
        self.rect = pygame.rect.Rect((x, y), ENEMY_IMG.get_size())

    def move(self, player_pos):
        if player_pos[0] > self.rect.x:
            self.rect.x += self.speed_x
        elif player_pos[0] < self.rect.x:
            self.rect.x -= self.speed_x
        if player_pos[1] > self.rect.y:
            self.rect.y += self.speed_y
        elif player_pos[1] < self.rect.y:
            self.rect.y -= self.speed_y


class Player(Sprite):
    def __init__(self):
        super().__init__(PLAYER_IMG, 0, 0)
        self.rect = pygame.rect.Rect((0, 0), PLAYER_IMG.get_size())
        self.rect.center = (WIDTH/2, HEIGHT/2)  # Spawn in the center

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    @property
    def pos(self):
        return self.rect.x, self.rect.y


def main():
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    tick = 0

    player = Player()

    num_of_bullets = 50
    num_of_kills = 0
    bullets = []
    enemies = []

    while True:  # main loop
        if num_of_bullets <= 0:
            display.fill('black')
            text_surf = FONT.render('GAME OVER', True, (255, 255, 255))
            text_rect = text_surf.get_rect()
            text_rect.center = (WIDTH/2, HEIGHT/2)
            display.blit(text_surf, text_rect)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
            clock.tick(FPS)

            continue

        display.fill('white')
        player.move()
        player.draw(display)

        text_surf = FONT.render(str(num_of_bullets), True, (0, 0, 0))
        text_rect = text_surf.get_rect()
        text_rect.topleft = (10, 10)
        display.blit(text_surf, text_rect)

        text_surf = FONT.render(str(num_of_kills), True, (180, 0, 0))
        text_rect = text_surf.get_rect()
        text_rect.topleft = (10, 50)
        display.blit(text_surf, text_rect)

        if tick % FPS == 0:  # 每秒
            enemies.append(Enemy(ENEMY_IMG))

        for i in range(len(bullets)-1, -1, -1):
            print('processing bullet', i)
            bullet = bullets[i]
            bullet.move()
            bullet.draw(display)
            for j in range(len(enemies)-1, -1, -1):
                if bullet.collided_with(enemies[j]):
                    bullets.pop(i)
                    enemies.pop(j)
                    num_of_bullets += random.randint(1, 3)
                    num_of_kills += 1
                else:
                    display = bullet.draw(display)

        for j in range(len(enemies)-1, -1, -1):
            enemy = enemies[j]
            enemy.move(player.pos)
            enemy.draw(display)
            if enemy.collided_with(player):
                enemies.pop(j)
                num_of_bullets -= random.randint(5, 10)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                if event.key in (K_w, K_s):
                    player.speed_y = 0
                elif event.key in (K_a, K_d):
                    player.speed_x = 0
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    bullets.append(Bullet(0, -BULLET_SPEED, player.pos))
                    num_of_bullets -= 1
                elif event.key == K_DOWN:
                    bullets.append(Bullet(0, BULLET_SPEED, player.pos))
                    num_of_bullets -= 1
                elif event.key == K_LEFT:
                    bullets.append(Bullet(-BULLET_SPEED, 0, player.pos))
                    num_of_bullets -= 1
                elif event.key == K_RIGHT:
                    bullets.append(Bullet(BULLET_SPEED, 0, player.pos))
                    num_of_bullets -= 1

                elif event.key == K_w:
                    player.speed_y = -PLAYER_SPEED
                elif event.key == K_a:
                    player.speed_x = -PLAYER_SPEED
                elif event.key == K_s:
                    player.speed_y = PLAYER_SPEED
                elif event.key == K_d:
                    player.speed_x = PLAYER_SPEED

        tick += 1
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
