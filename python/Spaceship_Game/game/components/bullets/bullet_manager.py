from game.components.explosions.explosion import Explosion


class BulletManager:

    def __init__(self) -> None:
        self.enemy_bullets = []
        self.player_bullets = []

    def update(self, game) -> None:
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if (
                bullet.rect.colliderect(game.player.rect)
                and bullet.owner.type == "enemy" 
            ):
                if not game.player.has_power_up:
                    explosion = Explosion(game.player)
                    game.explotion_manager.add_explosion(explosion)
                self.enemy_bullets.remove(bullet)

        for bullet in self.player_bullets:
            bullet.update(self.player_bullets)

            for enemy in game.enemy_manager.enemies:
                if (
                    bullet.rect.colliderect(enemy.rect)
                    and bullet.owner.type == "player"
                ):
                    self.player_bullets.remove(bullet)
                    explosion = Explosion(enemy)
                    game.explotion_manager.add_explosion(explosion)
                    game.enemy_manager.enemies.remove(enemy)
                    game.player.score += 1

    def draw(self, screen) -> None:
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        for bullet in self.player_bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet) -> None:
        if bullet.owner.type == "player" and len(self.player_bullets) < 4:
            self.player_bullets.append(bullet)
        elif bullet.owner.type == "enemy" and len(self.enemy_bullets) < 4:
            self.enemy_bullets.append(bullet)

    def reset(self) -> None:
        self.enemy_bullets = []
        self.player_bullets = []
