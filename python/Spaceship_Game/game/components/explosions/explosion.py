import pygame
from pygame.sprite import Sprite

from game.utils.constants import EXPLOSION, EXPLOSION_SOUND


class Explosion(Sprite):
    def __init__(self, spaceship):
        self.image = EXPLOSION
        self.sound = pygame.mixer.Sound(EXPLOSION_SOUND)
        self.spaceship = spaceship
        self.rect = self.image.get_rect()
        self.rect.center = self.spaceship.rect.center

        self.life = pygame.time.get_ticks() + 200

    def update(self):
        if self.spaceship.type == "player":
            self.rect.center = self.spaceship.rect.center
        self.rect.y += 10

    def draw(self, screen):
        screen.blit(self.image, self.rect)
