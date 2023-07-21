import pygame
import os


# Global Constants
TITLE = "Spaceships Game"
FONT_STYLE = "freesansbold.ttf"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN_HEIGHT_CENTER = SCREEN_HEIGHT // 2
SCREEN_WIDTH_CENTER = SCREEN_WIDTH // 2

FPS = 30
ROOT_DIR = os.path.join(os.path.dirname(__file__), "../..")
IMG_DIR = os.path.join(os.path.dirname(__file__), ROOT_DIR, "game/assets/img")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Other/shield.png"))

BG = pygame.image.load(os.path.join(IMG_DIR, "Other/Track.png"))

HEART = pygame.image.load(os.path.join(IMG_DIR, "Other/SmallHeart.png"))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"

SHIP_WIDTH = 40
SHIP_HEIGHT = 60
SHIP_X_POS = SCREEN_WIDTH_CENTER - SHIP_WIDTH
SHIP_Y_POS = 500
SHIP_SPEED = 10
SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(
    os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png")
)

BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))
BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
EXPLOSION = pygame.image.load(os.path.join(IMG_DIR, "Other/explosion.gif"))

ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
ENEMIES = [
    {
        "image": ENEMY_1,
        "speed_x": 5,
        "speed_y": 1,
        "shooting_interval": 1000,
    },
    {"image": ENEMY_2, "speed_x": 7, "speed_y": 2, "shooting_interval": 500},
]

COLORS = {
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0),
}

# Sounds

AUDIO_DIR = os.path.join(os.path.dirname(__file__), "..", "assets/audio")

SPACESHIP_SHOOT_SOUND = os.path.join(AUDIO_DIR, "spaceship_shoot.wav")
POWER_UP_SOUND = os.path.join(AUDIO_DIR, "power_up.wav")
GAME_OVER_SOUND = os.path.join(AUDIO_DIR, "game_over.wav")
OPENER_SOUND = os.path.join(AUDIO_DIR, "game_opener.wav")
EXPLOSION_SOUND = os.path.join(AUDIO_DIR, "explosion.wav")

BACKGROUND_SOUND = os.path.join(AUDIO_DIR, "menu.mp3")
