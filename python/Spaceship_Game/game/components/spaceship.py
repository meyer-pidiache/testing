import pygame
from pygame.sprite import Sprite

from game.components.bullets.bullet import Bullet
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, SHIP_WIDTH, SHIP_HEIGHT, SCREEN_WIDTH_CENTER, SCREEN_HEIGHT_CENTER, DEFAULT_TYPE

class Spaceship(Sprite):
    X_POS = SCREEN_WIDTH_CENTER - SHIP_WIDTH
    Y_POS = 500
    SHIP_SPEED = 10
    
    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (SHIP_WIDTH, SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

        self.score = 0
        self.highest_score = 0
        self.death_count = 0

        self.type = 'player'
        self.last_shoot_time = 0
        self.shooting_interval = 250

        self.power_up_type = DEFAULT_TYPE
        self.has_power_up = False
        self.power_time_up = 0

    def update(self, user_input, game):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()
        if user_input[pygame.K_SPACE]:
            self.shoot(game.bullet_manager)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shoot_time >= self.shooting_interval:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.last_shoot_time = current_time

    def move_left(self):
        self.rect.x -= self.SHIP_SPEED
        if self.rect.left < -70:
            self.rect.x = SCREEN_WIDTH
    
    def move_right(self):
        self.rect.x += self.SHIP_SPEED
        if self.rect.right > SCREEN_WIDTH + 70:
            self.rect.x = -70

    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT_CENTER:
            self.rect.y -= self.SHIP_SPEED

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 70:
            self.rect.y += self.SHIP_SPEED

    def reset(self):
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.score = 0

    def set_image(self, size = (40, 60), image = SPACESHIP):
        self.image = image
        self.image = pygame.transform.scale(self.image, size)