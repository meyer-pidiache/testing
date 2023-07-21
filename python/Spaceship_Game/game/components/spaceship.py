import os
import pickle
import pygame
from pygame.sprite import Sprite

from game.utils.constants import (
    SPACESHIP,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    SHIP_WIDTH,
    SHIP_HEIGHT,
    SHIP_SPEED,
    SHIP_X_POS,
    SHIP_Y_POS,
    SCREEN_HEIGHT_CENTER,
    DEFAULT_TYPE,
    SPACESHIP_SHOOT_SOUND,
)
from game.components.bullets.bullet import Bullet


class Spaceship(Sprite):
    
    def __init__(self) -> None:
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (SHIP_WIDTH, SHIP_HEIGHT))
        self.sound = pygame.mixer.Sound(SPACESHIP_SHOOT_SOUND)
        self.rect = self.image.get_rect()
        self.rect.x = SHIP_X_POS
        self.rect.y = SHIP_Y_POS

        self.score = 0
        self.highest_score = 0
        self.death_count = 0

        self.type = "player"
        self.last_shoot_time = 0
        self.shooting_interval = 250

        self.power_up_type = DEFAULT_TYPE
        self.has_power_up = False
        self.power_time_up = 0

        self.load_highest_score()

    def update(self, user_input, game) -> None:
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

        for enemy in game.enemy_manager.enemies:
            if self.rect.colliderect(enemy.rect) and not self.has_power_up:
                game.game_over()

    def draw(self, screen) -> None:
        screen.blit(self.image, self.rect)

    def shoot(self, bullet_manager) -> None:
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shoot_time >= self.shooting_interval:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.sound.play()
            self.last_shoot_time = current_time

    def move_left(self) -> None:
        self.rect.x -= SHIP_SPEED
        if self.rect.left < -70:
            self.rect.x = SCREEN_WIDTH

    def move_right(self) -> None:
        self.rect.x += SHIP_SPEED
        if self.rect.right > SCREEN_WIDTH + 70:
            self.rect.x = -70

    def move_up(self) -> None:
        if self.rect.y > SCREEN_HEIGHT_CENTER:
            self.rect.y -= SHIP_SPEED

    def move_down(self) -> None:
        if self.rect.y < SCREEN_HEIGHT - 70:
            self.rect.y += SHIP_SPEED

    def reset(self) -> None:
        self.rect.x = SHIP_X_POS
        self.rect.y = SHIP_Y_POS
        self.score = 0

    def set_image(self, size=(40, 60), image=SPACESHIP) -> None:
        self.image = image
        self.image = pygame.transform.scale(self.image, size)

    def load_highest_score(self) -> None:
        try:
            with open("data/score.bin", "rb") as file:
                self.highest_score = pickle.load(file)
        except:
            self.highest_score = 0

    def save_highest_score(self) -> None:
        if not os.path.exists("data"):
            os.makedirs("data")
        with open("data/score.bin", "wb") as file:
            pickle.dump(self.highest_score, file)
