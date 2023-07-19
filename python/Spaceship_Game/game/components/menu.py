import pygame

from game.utils.constants import FONT_STYLE, SCREEN_WIDTH, SCREEN_HEIGHT

class Menu:
    def __init__(self, message, screen):
        self.reset_screen_color(screen)
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def update(self, game):
        pygame.display.update()
        self.handle_event_on_menu(game)

    def draw(self, screen):
        screen.blit(self.text, self.text_rect)

    def handle_event_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            elif event.type == pygame.KEYDOWN:
                game.run()

    def reset_screen_color(self, screen):
        screen.fill((255, 255, 255))

    def update_message(self, message):
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
