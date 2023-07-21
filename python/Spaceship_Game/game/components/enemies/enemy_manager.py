from random import choice

from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMIES


class EnemyManager:

    def __init__(self) -> None:
        self.enemies = []

    def update(self, game) -> None:
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies, game)

    def draw(self, screen) -> None:
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self) -> None:
        if len(self.enemies) < 2:
            enemy = Enemy(*self.get_random_enemy_data())
            self.enemies.append(enemy)

    def get_random_enemy_data(self) -> None:
        enemy = choice(ENEMIES)
        return enemy.values()

    def reset(self) -> None:
        self.enemies = []
