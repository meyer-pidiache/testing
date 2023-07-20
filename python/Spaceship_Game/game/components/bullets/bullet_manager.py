import pygame

class BulletManager:
    def __init__(self):
        self.enemy_bullets = []
        self.player_bullets = []

    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player.rect) and bullet.owner.type == 'enemy':
                self.enemy_bullets.remove(bullet)

                if not game.player.has_power_up:
                    game.game_over()
        
        for bullet in self.player_bullets:
            bullet.update(self.player_bullets)

            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner.type == 'player':
                    self.player_bullets.remove(bullet)
                    game.enemy_manager.enemies.remove(enemy)
                    game.player.score += 1

    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        for bullet in self.player_bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner.type == 'player' and len(self.player_bullets) < 4:
            self.player_bullets.append(bullet)
        elif bullet.owner.type == 'enemy' and len(self.enemy_bullets) < 4:
            self.enemy_bullets.append(bullet)

    def reset(self):
        self.enemy_bullets = []
        self.player_bullets = []
