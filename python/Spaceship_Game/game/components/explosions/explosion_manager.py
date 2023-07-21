import pygame


class ExplosionManager:

    def __init__(self) -> None:
        self.explosions = []

    def update(self, game) -> None:
        for explosion in self.explosions:
            explosion.update()

            now = pygame.time.get_ticks()
            if now >= explosion.life:
                if explosion.spaceship.type == "player":
                    game.game_over()
                    break
                else:
                    self.explosions.remove(explosion)

    def draw(self, screen) -> None:
        for explosion in self.explosions:
            explosion.draw(screen)

    def add_explosion(self, explosion) -> None:
        explosion.sound.play()
        self.explosions.append(explosion)

    def reset(self) -> None:
        self.explosions = []
