import pygame

from game.utils.constants import FONT_STYLE, ICON, COLORS, SCREEN_HEIGHT_CENTER, SCREEN_WIDTH_CENTER

class Menu:
    def __init__(self, lines, screen):
        self.reset_screen_color(screen)
        self.icon = pygame.transform.scale(ICON, (80, 120))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text_lines = [self.font_render(line, COLORS['BLACK']) for line in lines]

    def update(self, game):
        pygame.display.update()
        self.handle_event_on_menu(game)

    def draw(self, screen):
        screen.blit(self.icon, (SCREEN_WIDTH_CENTER - 40, SCREEN_HEIGHT_CENTER - 150))
        counter = 0
        for line in self.text_lines:
            line_rect = line.get_rect()
            line_rect.center = (SCREEN_WIDTH_CENTER, SCREEN_HEIGHT_CENTER + counter)
            screen.blit(line, line_rect)
            counter += 40

    def handle_event_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            elif event.type == pygame.KEYDOWN:
                game.run()

    def reset_screen_color(self, screen):
        screen.fill(COLORS['WHITE'])

    def update_message(self, lines):
        self.text_lines = [self.font_render(line, COLORS['BLACK']) for line in lines]

    def font_render(self, line, color):
        return self.font.render(line, True, color)
