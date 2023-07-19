import pygame
from random import randint
from pygame.sprite import Sprite

from game.utils.constants import SHIP_WIDTH, SHIP_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT
from game.components.bullets.bullet import Bullet
from game.components.bullets.bullet_manager import BulletManager

class Enemy(Sprite):
    Y_POS = 20
    MOV_X = {0: 'left', 1: 'right'}

    def __init__(self, image, speed_x, speed_y, shooting_interval) -> None:
        self.image = image
        self.image = pygame.transform.scale(self.image, (SHIP_WIDTH, SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, SCREEN_WIDTH)
        self.rect.y = self.Y_POS

        self.speed_x = speed_x
        self.speed_y = speed_y
        self.movement_x = self.MOV_X[randint(0, 1)]
        self.movement_x_for = randint(30, 40)
        self.step = 0
        self.type = 'enemy'
        self.bullets = []
        self.bullet_manager = BulletManager(self)
        self.last_shoot_time = 0
        self.shooting_interval = shooting_interval

    def update(self, enemies, game):
        self.bullet_manager.update(game)
        self.rect.y += self.speed_y
        self.shoot()
        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x
        self.change_movement_x()

        if self.rect.y >= SCREEN_HEIGHT:
            enemies.remove(self)

    def draw(self, screen):
        self.bullet_manager.draw(screen)
        screen.blit(self.image, self.rect)

    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shoot_time >= self.shooting_interval and len(self.bullets) < 2:
            bullet = Bullet(self)
            self.bullets.append(bullet)
            self.last_shoot_time = current_time

    def change_movement_x(self):
        self.step += 1

        if self.step >= self.movement_x_for and self.movement_x == 'right' or self.rect.x >= SCREEN_WIDTH - SHIP_WIDTH:
            self.movement_x = 'left'
            self.step = 0

        if self.step >= self.movement_x_for and self.movement_x == 'left' or self.rect.x <= 10:
            self.movement_x = 'right'
            self.step = 0
