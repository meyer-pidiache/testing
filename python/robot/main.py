robot_art = r"""
      0: {head_name}
      Is available: {head_status}
      Attack: {head_attack}
      Defense: {head_defense}
      Energy consumption: {head_energy_consump}
              ^
              |                  |1: {weapon_name}
              |                  |Is available: {weapon_status}
     ____     |    ____          |Attack: {weapon_attack}
    |oooo|  ____  |oooo| ------> |Defense: {weapon_defense}
    |oooo| '    ' |oooo|         |Energy consumption: {weapon_energy_consump}
    |oooo|/\_||_/\|oooo|
    `----' / __ \  `----'           |2: {left_arm_name}
   '/  |#|/\/__\/\|#|  \'           |Is available: {left_arm_status}
   /  \|#|| |/\| ||#|/  \           |Attack: {left_arm_attack}
  / \_/|_|| |/\| ||_|\_/ \          |Defense: {left_arm_defense}
 |_\/    O\=----=/O    \/_|         |Energy consumption: {left_arm_energy_consump}
 <_>      |=\__/=|      <_> ------> |
 <_>      |------|      <_>         |3: {right_arm_name}
 | |   ___|======|___   | |         |Is available: {right_arm_status}
// \\ / |O|======|O| \  //\\        |Attack: {right_arm_attack}
|  |  | |O+------+O| |  |  |        |Defense: {right_arm_defense}
|\/|  \_+/        \+_/  |\/|        |Energy consumption: {right_arm_energy_consump}
\__/  _|||        |||_  \__/
      | ||        || |          |4: {left_leg_name}
     [==|]        [|==]         |Is available: {left_leg_status}
     [===]        [===]         |Attack: {left_leg_attack}
      >_<          >_<          |Defense: {left_leg_defense}
     || ||        || ||         |Energy consumption: {left_leg_energy_consump}
     || ||        || || ------> |
     || ||        || ||         |5: {right_leg_name}
   __|\_/|__    __|\_/|__       |Is available: {right_leg_status}
  /___n_n___\  /___n_n___\      |Attack: {right_leg_attack}
                                |Defense: {right_leg_defense}
                                |Energy consumption: {right_leg_energy_consump}

"""

class Part:
    def __init__(self, name, attack_level=0, defense_level=0, energy_comsuption=0):
        # Constructor
        self.name = name
        self.attack_level = attack_level
        self.defense_level = defense_level
        self.energy_comsuption = energy_comsuption

    def get_status_dict(self):
        # Obtener el estado de la parte en un diccionario
        formatted_name = self.name.replace(" ", "_").lower()

        return {
            "{}_name".format(formatted_name): self.name.upper(),
            "{}_status".format(formatted_name): self.is_available(),
            "{}_attack".format(formatted_name): self.attack_level,
            "{}_defense".format(formatted_name): self.defense_level,
            "{}_energy_consump".format(formatted_name): self.energy_comsuption,
        }

    def is_available(self):
        # Verificar que la parte esté funcional
        return not self.defense_level <= 0

import random
from time import sleep

colors = {
    "Black": "\x1b[90m",
    "Blue": "\x1b[94m",
    "Cyan": "\x1b[96m",
    "Green": "\x1b[92m",
    "Magenta": "\x1b[95m",
    "Red": "\x1b[91m",
    "White": "\x1b[97m",
    "Yellow": "\x1b[93m",
}


class Robot:
    def __init__(self, name, color_code):
        self.name = name
        self.color_code = color_code
        self.energy = 100
        self.coins = 100
        self.previous_roll = 0
        self.dice = Dice(0, "Normal_dice", 0, [1, 2, 3, 4, 5, 6])
        self.parts = [
            Part("Head", attack_level=5, defense_level=200, energy_comsuption=5),
            Part("Weapon", attack_level=15, defense_level=10, energy_comsuption=10),
            Part("Left Arm", attack_level=3, defense_level=20, energy_comsuption=10),
            Part("Right Arm", attack_level=6, defense_level=20, energy_comsuption=10),
            Part("Left Leg", attack_level=4, defense_level=20, energy_comsuption=15),
            Part("Right Leg", attack_level=8, defense_level=20, energy_comsuption=15),
        ]

    def greet(self):
        print("Hello, my name is:", self.name)

    def print_energy(self):
        print(f"We have {self.energy} percent energy left.")

    def attack(self, enemy_robot, part_to_use, part_to_attack):
        enemy_robot.parts[part_to_attack].defense_level -= self.parts[
            part_to_use
        ].attack_level
        self.energy -= self.parts[part_to_use].energy_comsuption

    def is_on(self):
        return self.energy >= 0

    def is_there_available_parts(self):
        for part in self.parts:
            if part.is_available():
                return True
            return False

    def print_status(self, round):

        print(colors["Green"], end="")
        print(f"""\n
            #################################
            ############ ROUND {round} ############
            #################################
            """
        )
        print(colors["White"], end="")

        print(self.color_code)
        str_robot = robot_art.format(**self.get_part_status())
        self.greet()
        self.print_energy()
        print(str_robot)
        print(colors["White"])

    def get_part_status(self):
        part_status = {}
        for part in self.parts:
            status_dict = part.get_status_dict()
            part_status.update(status_dict)

        return part_status

    def increse_level(self, part_to_power, dice_number):
        # Aumentar nivel de defensa o de ataque de acuerdo al dado

        is_even = dice_number % 2 == 0

        if is_even:
            self.parts[part_to_power].attack_level *= dice_number
        else:
            self.parts[part_to_power].defense_level *= dice_number

        return (dice_number, is_even)

    def buy_dice(self, store, dice_option):
        # Se compra un dado y se reemplaza por el actual
        self.dice = store.get_dice(dice_option)
        self.coins -= self.dice.price

    def decrease_level(self, part_to_power, dice_number):
        # Aumentar nivel de defensa o de ataque de acuerdo al dado

        is_even = dice_number % 2 == 0

        # Deja los valores por defecto
        if is_even:
            self.parts[part_to_power].attack_level //= dice_number
        else:
            self.parts[part_to_power].defense_level //= dice_number


class Dice:
    DICE_ART_DICT = {
        1: """
      +-------+
      |       |
      |   *   |
      |       |
      +-------+
    """,
        2: """
      +-------+
      | *     |
      |       |
      |     * |
      +-------+
    """,
        3: """
      +-------+
      | *     |
      |   *   |
      |     * |
      +-------+
    """,
        4: """
      +-------+
      | *   * |
      |       |
      | *   * |
      +-------+
    """,
        5: """
      +-------+
      | *   * |
      |   *   |
      | *   * |
      +-------+
    """,
        6: """
      +-------+
      | *   * |
      | *   * |
      | *   * |
      +-------+
    """,
    }

    def __init__(self, id, name, price, sides_list):
        self.id = id
        self.name = name
        self.price = price
        self.sides = sides_list

    def roll_dice(self, current_robot, enemy_robot):
        print("Throwing the dice...", end=" ")
        sleep(4)
        dice_number = random.choice(self.sides)
        print(f"The dice shows {dice_number}", end="")

        print(colors["Yellow"])
        print(self.DICE_ART_DICT[dice_number])
        print(colors["White"], end="")


        if dice_number == current_robot.previous_roll:
            print(f"{current_robot.name} sorry, you lose :(\n")
            print(f"\nCongratulations {enemy_robot.name}, you won :D!")
            exit()

        self.previous_roll = dice_number

        return dice_number

    def show_dice(self):
        print(f". {self.name}. Price: {self.price}. Sides: {self.sides}")

class Store:
    def __init__(self) -> None:
        self.normal_dice = Dice(0, "Normal Dice", 0, [1, 2, 3, 4, 5, 6])
        self.even_dice = Dice(1, "Even Dice", 75, [2, 4, 6])
        self.odd_dice = Dice(2, "Odd Dice", 75, [1, 3, 5])
        self.dices = [self.normal_dice, self.even_dice, self.odd_dice]

    def get_dice(self, dice_number):
        # Retorna el dado según el número indicado
        for dice in self.dices:
            if dice_number == dice.id:
                return dice

    def get_minimium_price(self):
        values = []
        for dice in self.dices:
            values.append(dice.price)

        return min(values)

class Game:
    def __init__(self, robot_one, robot_two):
        self.robot_one = robot_one
        self.robot_two = robot_two
        self.store = Store()
        self.playing = True
        self.round = 0

        print("Welcome to the game!")

    def get_user_input(self, message, valid_elements):
        print(f"{colors['Cyan']}{message} {valid_elements}:\n")
        user_input = input()

        valid_elements = [str(element) for element in valid_elements]

        while not user_input in valid_elements:
            print(f"\n{colors['Red']}Invalid input, type again:\n")
            user_input = input()

        print(colors["White"], end="")
        return user_input

    def play_game(self):
        parts_number = [0, 1, 2, 3, 4, 5]

        while self.playing:
            if self.round % 2 == 0:
                current_robot = self.robot_one
                enemy_robot = self.robot_two
            else:
                current_robot = self.robot_two
                enemy_robot = self.robot_one

            self.round += 1

            current_robot.print_status(self.round)
            self.offer_dices(current_robot)

            dice_number = current_robot.dice.roll_dice(current_robot, enemy_robot)

            # Aumentar nivel
            action = 'attack' if dice_number % 2 == 0 else 'deffense'
            part_power_current = int(
                self.get_user_input(f"Choose a part to increase the level of {action}", parts_number)
            )
            current_robot.increse_level(part_power_current, dice_number)

            current_robot.print_status(self.round)
            part_to_use = int(
                self.get_user_input("What part should I use to attack?", parts_number)
            )

            enemy_robot.print_status(self.round)
            part_to_attack = int(
                self.get_user_input("Choose a enemy part to attack", parts_number)
            )

            current_robot.attack(enemy_robot, part_to_use, part_to_attack)

            current_robot.decrease_level(part_power_current, dice_number)

            if (
                not enemy_robot.is_on()
                or enemy_robot.is_there_available_parts() == False
            ):
                self.playing = False
                print(f"\nCongratulations {current_robot.name}, you won :D!")

    def offer_dices(self, current_robot):
        # Revisar billetera (método)
        if current_robot.coins >= self.store.get_minimium_price():
            dice_decision = self.get_user_input(
                "Do you want to buy a dice?", ["True", "False"]
            )

            if dice_decision == "True":
                # Comprar dado desde la tienda
                print()
                counter = 1
                for dice in self.store.dices[1:]:
                    print(counter, end="")
                    dice.show_dice()
                    counter += 1

                dice_option = int(self.get_user_input("\nEnter dice number", [1, 2]))

                current_robot.buy_dice(self.store, dice_option)

            print("")

def main():
    robot_one = Robot("Jarvis", colors["Blue"])
    robot_two = Robot("Friday", colors["Magenta"])

    game = Game(robot_one, robot_two)

    game.play_game()

main()

