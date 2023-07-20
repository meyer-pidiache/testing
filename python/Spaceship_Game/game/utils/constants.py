import pygame
import os
from random import randint

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN_HEIGHT_CENTER = SCREEN_HEIGHT // 2
SCREEN_WIDTH_CENTER = SCREEN_WIDTH // 2

FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

SHIP_WIDTH = 40
SHIP_HEIGHT = 60

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
ENEMIES = [
    {
        'image': ENEMY_1,
        'speed_x': 5,
        'speed_y': 1,
        'shooting_interval': 1000,
    }, 
    {
        'image': ENEMY_2,
        'speed_x': 7,
        'speed_y': 2,
        'shooting_interval': 500
    }, 
]

FONT_STYLE = 'freesansbold.ttf'

COLORS = {
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0),
}
