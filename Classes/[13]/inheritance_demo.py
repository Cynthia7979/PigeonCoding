import random, pygame

WIDTH, HEIGHT = 1000, 800
enemy_img = pygame.surface.Surface((20, 60))
enemy_img.fill('red')


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