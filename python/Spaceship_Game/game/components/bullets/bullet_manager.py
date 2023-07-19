import pygame

class BulletManager:
    def __init__(self, spaceship):
        self.bullets = spaceship.bullets

    def update(self, game):
        for bullet in self.bullets:
            bullet.update()

            if bullet.rect.colliderect(game.player.rect) and bullet.owner.type == 'enemy':
                self.bullets.remove(bullet)

                game.playing = False
                game.death_count += 1
                pygame.time.delay(1000)
                break

            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner.type == 'player':
                    self.bullets.remove(bullet)
                    game.enemy_manager.enemies.remove(enemy)
                    game.score += 1

    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)
