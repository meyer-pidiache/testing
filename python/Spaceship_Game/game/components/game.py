import pygame

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE, COLORS, DEFAULT_TYPE
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager
from game.components.menu import Menu
from game.components.power_ups.power_up_manager import PowerUpManager


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.running = False
        self.menu = Menu(["Press any key to start..."], self.screen)
        self.power_up_manager = PowerUpManager()

    def execute(self):
        self.running = True

        while self.running:
            if not self.playing:
                self.show_menu()
        
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        self.power_up_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def show_menu(self):
        self.menu.reset_screen_color(self.screen)
        
        if self.player.death_count == 0:
            self.menu.draw(self.screen)
        else:
            lines = [
                'Game Over. Press any key to restart',
                f'Your score: {self.player.score}',
                f'Highest score: {self.player.highest_score}',
                f'Total deaths: {self.player.death_count}',
            ]
            self.menu.update_message(lines)
            self.menu.draw(self.screen)

        self.menu.update(self)

    def draw_score(self):
        text = self.font.render(f'Score: {self.player.score}', True, COLORS['WHITE'])
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)


    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks()) / 1000, 2)

            if time_to_show >= 0:
                text = self.font.render(f'{self.player.power_up_type}: {time_to_show}', True, COLORS['WHITE'])
                text_rect = text.get_rect()
                text_rect = (50, 25)
                self.screen.blit(text, text_rect)
            else:
                self.player.has_power_up = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.set_image()

    def game_over(self):
        self.playing = False
        self.player.death_count += 1

        if self.player.score > self.player.highest_score:
            self.player.highest_score = self.player.score

        pygame.time.delay(1000)

        self.reset()

    def reset(self):
        self.enemy_manager.reset()
        self.bullet_manager.reset()
        self.player.reset()
        self.power_up_manager.reset()
