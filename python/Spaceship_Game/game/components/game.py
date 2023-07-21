import pygame

from game.utils.constants import (
    BG,
    ICON,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TITLE,
    FPS,
    FONT_STYLE,
    COLORS,
    DEFAULT_TYPE,
    GAME_OVER_SOUND,
    OPENER_SOUND,
    BACKGROUND_SOUND,
)
from game.components.bullets.bullet_manager import BulletManager
from game.components.enemies.enemy_manager import EnemyManager
from game.components.explosions.explosion_manager import ExplosionManager
from game.components.spaceship import Spaceship
from game.components.power_ups.power_up_manager import PowerUpManager
from game.components.menu import Menu


class Game:
    
    def __init__(self) -> None:
        ## Inicializar pygame
        pygame.mixer.pre_init(44100, 32, 2, 1024)
        pygame.init()

        pygame.display.set_icon(ICON)
        pygame.display.set_caption(TITLE)

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.clock = pygame.time.Clock()

        self.opener_sound = pygame.mixer.Sound(OPENER_SOUND)
        self.game_over_sound = pygame.mixer.Sound(GAME_OVER_SOUND)
        pygame.mixer.music.load(BACKGROUND_SOUND)
        pygame.mixer.music.play(100)

        self.bullet_manager = BulletManager()
        self.enemy_manager = EnemyManager()
        self.explotion_manager = ExplosionManager()
        self.player = Spaceship()
        self.power_up_manager = PowerUpManager()
        self.menu = Menu(self.screen)

        self.running = False
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0

    def execute(self) -> None:
        self.running = True

        while self.running:
            if not self.playing:
                self.show_menu()

        self.player.save_highest_score()
        pygame.display.quit()
        pygame.quit()

    def run(self) -> None:
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self) -> None:
        user_input = pygame.key.get_pressed()

        self.player.update(user_input, self)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        self.power_up_manager.update(self)
        self.explotion_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)

        self.screen.fill(COLORS["WHITE"])
        self.draw_background()

        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.explotion_manager.draw(self.screen)

        self.draw_power_up_time()
        self.draw_score()

        pygame.display.update()

    def draw_background(self) -> None:
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))

        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def show_menu(self) -> None:
        pygame.mixer.music.unpause()
        self.menu.reset_screen_color(self.screen)

        if self.player.death_count == 0:
            self.menu.draw(self.screen)
        else:
            lines = [
                "Game Over. Press [ENTER] to restart",
                f"Your score: {self.player.score}",
                f"Highest score: {self.player.highest_score}",
                f"Total deaths: {self.player.death_count}",
            ]
            self.menu.update_message(lines)
            self.menu.draw(self.screen)

        self.menu.update(self)

    def draw_score(self) -> None:
        text = self.font.render(f"Score: {self.player.score}", True, COLORS["WHITE"])
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

    def draw_power_up_time(self) -> None:
        if self.player.has_power_up:
            time_to_show = round(
                (self.player.power_time_up - pygame.time.get_ticks()) / 1000, 2
            )

            if time_to_show >= 0:
                text = self.font.render(
                    f"{self.player.power_up_type.capitalize()}: {time_to_show}",
                    True,
                    COLORS["WHITE"],
                )
                text_rect = text.get_rect()
                text_rect = (50, 25)
                self.screen.blit(text, text_rect)
            else:
                self.player.has_power_up = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.set_image()

    def game_over(self) -> None:
        self.game_over_sound.play()
        self.playing = False
        self.player.death_count += 1

        if self.player.score > self.player.highest_score:
            self.player.highest_score = self.player.score

        pygame.time.delay(1000)

        self.reset()

    def reset(self) -> None:
        self.enemy_manager.reset()
        self.bullet_manager.reset()
        self.player.reset()
        self.power_up_manager.reset()
        self.explotion_manager.reset()
