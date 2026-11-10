import os
import art
from calculations import attack, enemy_attack, healing
from data import PHY_MOVES, MAGIC_MOVES
from itertools import zip_longest

menu_stages = {"start_menu": True, "new_game": False}
game_stages = {"start_message": False, "tutorial": False}
round_stages = {
    "round": False,
    "menu_selection": False,
    "action_summary": False,
    "enemies_turn": False,
    "upgrades": False,
}

# ENEMIES
GOBLIN = {
    "name": "Goblin",
    "hp": 50,
    "attack": {"name": "swipe", "dmg": 25, "type": "physical"},
    "phy_def": 10,
    "magic_def": 10,
    "art": art.GOBLIN,
}
SKELETON = {
    "name": "Skeleton",
    "hp": 40,
    "attack": {"name": "bow shot", "dmg": 25, "type": "physical"},
    "phy_def": 5,
    "magic_def": 10,
    "art": art.SKELETON,
}
ZOMBIE = {
    "name": "Zombie",
    "hp": 75,
    "attack": {"name": "bite", "dmg": 30, "type": "physical"},
    "phy_def": 10,
    "magic_def": 5,
    "art": art.ZOMBIE,
}
GHOST = {
    "name": "Ghost",
    "hp": 100,
    "attack": {"name": "haunt", "dmg": 25, "type": "magic"},
    "phy_def": 25,
    "magic_def": 10,
    "art": art.GHOST,
}
WITCH = {
    "name": "Witch",
    "hp": 60,
    "attack": {"name": "curse", "dmg": 35, "type": "magic"},
    "phy_def": 10,
    "magic_def": 30,
    "art": art.WITCH,
}
# Bosses
CENTAUR = {
    "name": "Centaur",
    "hp": 200,
    "attack": {"name": "kick", "dmg": 25, "type": "physical"},
    "phy_def": 20,
    "magic_def": 5,
    "art": art.CENTAUR,
}
GRIM_REAPER = {
    "name": "The Grim Reaper",
    "hp": 125,
    "attack": {"name": "soul harvest", "dmg": 35, "type": "magic"},
    "phy_def": 10,
    "magic_def": 15,
    "art": art.GRIM_REAPER,
}
DRAGON = {
    "name": "Dragon",
    "hp": 150,
    "attack1": {"name": "fire breath", "dmg": 40, "type": "magic"},
    "attack2": {"name": "tail whip", "dmg": 40, "type": "physical"},
    "phy_def": 25,
    "magic_def": 25,
    "art": art.DRAGON,
}

STARTING_MOVE_SET = [
    {
        "name": "Wizard",
        "move_1": PHY_MOVES[0],
        "move_2": MAGIC_MOVES[0],
        "move_3": MAGIC_MOVES[2],
        "move_4": MAGIC_MOVES[6],
    },
    {
        "name": "Magic Knight",
        "move_1": PHY_MOVES[0],
        "move_2": PHY_MOVES[6],
        "move_3": MAGIC_MOVES[0],
        "move_4": MAGIC_MOVES[1],
    },
    {
        "name": "Warrior",
        "move_1": PHY_MOVES[1],
        "move_2": PHY_MOVES[2],
        "move_3": PHY_MOVES[6],
        "move_4": MAGIC_MOVES[0],
    },
]

STARTING_CLASSES = [
    {
        "name": "Wizard",
        "hp": 75,
        "max_hp": 75,
        "phy_dmg": 5,
        "phy_def": 10,
        "magic_dmg": 18,
        "magic_def": 18,
        "move_set": STARTING_MOVE_SET[0],
        "art": art.WIZARD,
    },
    {
        "name": "Magic Knight",
        "hp": 80,
        "max_hp": 80,
        "phy_dmg": 10,
        "phy_def": 12,
        "magic_dmg": 10,
        "magic_def": 12,
        "move_set": STARTING_MOVE_SET[1],
        "art": art.KNIGHT,
    },
    {
        "name": "Warrior",
        "hp": 90,
        "max_hp": 90,
        "phy_dmg": 16,
        "phy_def": 18,
        "magic_dmg": 5,
        "magic_def": 10,
        "move_set": STARTING_MOVE_SET[2],
        "art": art.WARRIOR,
    },
]

ITEMS = [
    {"name": "Health Potion", "healing": 30, "lvl": 1},
    {"name": "Health Potion", "healing": 50, "lvl": 2},
]

ROUNDS = [
    {"enemies": [dict(GOBLIN)], "rewards": {"points": 3, "items": ITEMS[0]}},
    {
        "enemies": [dict(SKELETON), dict(SKELETON)],
        "rewards": {"points": 3, "items": "health_potion"},
    },
    {
        "enemies": [dict(GOBLIN), dict(ZOMBIE), dict(ZOMBIE)],
        "rewards": {"points": 5, "items": "health_potion"},
    },
    {"enemies": [dict(CENTAUR)], "rewards": {"points": 10, "items": "health_potion"}},
    {
        "enemies": [dict(GHOST), dict(GHOST), dict(GHOST)],
        "rewards": {"points": 5, "items": "health_potion"},
    },
    {
        "enemies": [dict(WITCH), dict(WITCH)],
        "rewards": {"points": 3, "items": "health_potion"},
    },
    {
        "enemies": [dict(GRIM_REAPER)],
        "rewards": {"points": 8, "items": "health_potion"},
    },
    {
        "enemies": [dict(SKELETON), dict(SKELETON), dict(ZOMBIE), dict(ZOMBIE)],
        "rewards": {"points": 5, "items": "health_potion"},
    },
    {
        "enemies": [dict(CENTAUR), dict(ZOMBIE), dict(GOBLIN)],
        "rewards": {"points": 8, "items": "health_potion"},
    },
    {"enemies": [dict(DRAGON)]},
]

current_round = ROUNDS[0]

player = {}

inventory = [dict(ITEMS[0])]


def menu():
    while True:
        msg = ""
        if menu_stages["start_menu"]:
            print_start_menu()
            menu_choice = input("\nChoose an option (1-4): ").strip()
            running = True
            while running:
                if menu_choice == "1":
                    print("No Current Save Available")
                    running = False
                elif menu_choice == "2":
                    menu_stages["start_menu"] = False
                    menu_stages["new_game"] = True
                    running = False
                elif menu_choice == "3":
                    pass
                elif menu_choice == "4":
                    return menu_choice
                else:
                    menu_choice = input("\nPlease Enter A Valid Choice (1-4): ").strip()

            input("\nPress Enter to continue...")
            os.system("clear")

        if menu_stages["new_game"]:
            running = True
            while running:
                msg, choice = new_game()
                if choice == "q":
                    menu_stages["start_menu"] = True
                    menu_stages["new_game"] = False
                    running = False
                    os.system("clear")

                if msg == "Start":
                    menu_stages["new_game"] = False
                    game_stages["start_message"] = True
                    round_stages["round"] = True
                    running = False
                    os.system("clear")
                    return dict(STARTING_CLASSES[int(choice) - 1])


def print_new_game_message():
    print("Welcome To The Beginning Of A New Journey")
    input("\nPress Enter to continue...")
    os.system("clear")
    print("Welcome To The Beginning Of A New Journey")
    print("You've Been Tasked With The Quest Of Slaying The Dragon")
    input("\nPress Enter to continue...")
    os.system("clear")
    print("Welcome To The Beginning Of A New Journey")
    print("You've Been Tasked With The Quest Of Slaying The Dragon")
    print("She Slumbers At The Other Side Of The Kingdom And Will Reek Havoc Upon Wake")
    input("\nPress Enter to continue...")
    os.system("clear")
    print("Welcome To The Beginning Of A New Journey")
    print("You've Been Tasked With The Quest Of Slaying The Dragon")
    print("She Slumbers At The Other Side Of The Kingdom And Will Reek Havoc Upon Wake")
    print("You Will Face Countless Hardships On Your Journey But You Must Succeed")
    input("\nPress Enter to continue...")
    os.system("clear")
    print("Welcome To The Beginning Of A New Journey")
    print("You've Been Tasked With The Quest Of Slaying The Dragon")
    print("She Slumbers At The Other Side Of The Kingdom And Will Reek Havoc Upon Wake")
    print("You Will Face Countless Hardships On Your Journey But You Must Succeed")
    print("Farewell And Good Luck")
    input("\nPress Enter to continue...")


def game(player):
    if game_stages["start_message"]:
        print_new_game_message()
        os.system("clear")
        game_stages["start_message"] = False
        round_stages["menu_selection"] = True

    if round_stages["round"]:
        game_interface(player, current_round)


def move_selection(move_set):
    print("-----------------")
    print("Move Set")
    print("-----------------")
    print(
        f"1. {move_set['move_1']['name']} Damage: {move_set['move_1']['dmg']} Target: {move_set['move_1']['target']}"
    )
    print(
        f"2. {move_set['move_2']['name']} Damage: {move_set['move_2']['dmg']} Target: {move_set['move_2']['target']}"
    )
    print(
        f"3. {move_set['move_3']['name']} Damage: {move_set['move_3']['dmg']} Target: {move_set['move_3']['target']}"
    )
    print(
        f"4. {move_set['move_4']['name']} Damage: {move_set['move_4']['dmg']} Target: {move_set['move_4']['target']}"
    )

    move = input("\nChoose an option (1-4, q to return): ").strip()

    while True:
        if move == "1":
            return move_set["move_1"]

        if move == "1":
            return move_set["move_2"]

        if move == "1":
            return move_set["move_3"]

        if move == "1":
            return move_set["move_4"]

        if move.lower() == "q":
            return "return"

        move = input("\nPlease Enter A Valid Choice (1-4): ").strip()


def target_selection(round):
    print("-----------------")
    print("Opponent(s)")
    print("-----------------")
    index = 1
    for enemy in round["enemies"]:
        print(f"{index}. {enemy['name']}")
        index += 1

    choice = input(f"\nChoose an option (1-{index - 1}, q to return): ").strip()
    while True:
        if choice.lower() == "q":
            return "return", None

        if choice.isdigit():
            if 0 < int(choice) <= (index - 1):
                return round["enemies"][int(choice) - 2], int(choice) - 2

        choice = input(f"\nPlease Enter A Valid Choice (1-{index - 1}): ").strip()


def print_game_menu(player, round):
    print(
        side_by_side(player["art"], *[enemies["art"] for enemies in round["enemies"]])
    )
    print("-----------------")
    enemies_hp = ""
    for enemies in round["enemies"]:
        enemies_hp += f"{enemies['name']}: {enemies['hp']} HP "

    print(f"HP: {player['hp']}{' ' * 10}{enemies_hp}")
    print("-----------------")


def print_inventory(inventory):
    print("-----------------")
    print("Inventory")
    print("-----------------")
    index = 1
    for item in inventory:
        print(
            f"{index}. {item['name']} (Level {item['lvl']}): Heals {item['healing']} HP"
        )
        index += 1

    choice = input(f"\nChoose an option (1-{index - 1}, q to return): ").strip()
    while True:
        if choice.lower() == "q":
            return "return"

        if choice.isdigit():
            if 0 < int(choice) <= (index - 1):
                return inventory[int(choice) - 2]

        choice = input(f"\nPlease Enter A Valid Choice (1-{index - 1}): ").strip()


def print_enemies_stats(round):
    for enemy in round["enemies"]:
        print("-----------------")
        print(enemy["name"])
        print("-----------------")
        print(f"Physical Defense: {enemy['phy_def']}")
        print(f"Magic Defense: {enemy['magic_def']}")


def check_for_round_end(round):
    return len(round["enemies"]) == 0


def game_interface(player, round):
    while round_stages["menu_selection"]:
        defend = False
        print_game_menu(player, round)
        print("1. Attack")
        print("2. Defend")
        print("3. Check")
        print("4. Items")
        menu_choice = input("\nChoose an option (1-4): ").strip()
        running = True
        while running:
            if menu_choice == "1":
                move = move_selection(player["move_set"])
                if move == "return":
                    break
                target, index = target_selection(round)
                if target == "return":
                    break
                dmg, status = attack(player, target, move)
                running = False
                round_stages["action_summary"] = True
                round_stages["menu_selection"] = False
            elif menu_choice == "2":
                print("-----------------")
                confirm = input("\nDefend(y/n)?: ").strip().lower()
                while True:
                    if confirm == "y":
                        defend = True
                        running = False
                        round_stages["action_summary"] = True
                        round_stages["menu_selection"] = False
                        break
                    elif confirm == "n":
                        running = False
                        break
                    else:
                        confirm = (
                            input("\nPlease Enter A Valid Choice(y/n): ")
                            .strip()
                            .lower()
                        )

            elif menu_choice == "3":
                print_enemies_stats(round)
                running = False
            elif menu_choice == "4":
                item = print_inventory(inventory)
                if item == "return":
                    break
                health_gained = healing(player, item)
                running = False
                round_stages["action_summary"] = True
                round_stages["menu_selection"] = False
            else:
                menu_choice = input("\nPlease Enter A Valid Choice (1-4): ").strip()

        input("\nPress Enter To Continue...")
        os.system("clear")

    while round_stages["action_summary"]:
        print_game_menu(player, round)
        if menu_choice == "1":
            print(f"{move['name']} dealt {dmg} damage to {target['name']}!")
            if status == "dead":
                print(f"{target['name']} has fallen!")
                round["enemies"].pop(index)
                if check_for_round_end(round):
                    print(
                        f"You earned {round['rewards']['points']} points and a Level {round['rewards']['items']['lvl']} {round['rewards']['items']['name']}!"
                    )
                    inventory.append(dict(round["rewards"]["items"]))
                    current_round = dict(ROUNDS[1])
                    round_stages["action_summary"] = False
                    round_stages["menu_selection"] = True
                    input("\nPress Enter to continue...")
                    os.system("clear")
                    break
        elif menu_choice == "2":
            print("You brace for an attack!")
        elif menu_choice == "4":
            print(
                f"Health Potion (Level {item['lvl']}) healed you for {health_gained} HP!"
            )

        input("\nPress Enter to continue...")
        os.system("clear")

        round_stages["action_summary"] = False
        round_stages["enemies_turn"] = True

    while round_stages["enemies_turn"]:
        print_game_menu(player, round)
        for enemy in round["enemies"]:
            dmg, move = enemy_attack(enemy, player, defend)
            print(
                f"{enemy['name']} uses {move['name']} ({move['type'].title()}) and does {dmg} dmg"
            )
            input("Press Enter To Continue...\n")

        os.system("clear")
        round_stages["enemies_turn"] = False
        round_stages["menu_selection"] = True


def side_by_side(*arts, gap=10):
    blocks = [a.splitlines() for a in arts]
    n = max(map(len, blocks))
    blocks = [[""] * (n - len(b)) + b for b in blocks]
    widths = [max(map(len, b)) for b in blocks]
    return "\n".join(
        (" " * gap).join(line.ljust(w) for line, w in zip(row, widths)).rstrip()
        for row in zip(*blocks)
    )


def tutorial():
    print("Welcome To The Tutorial!")
    input("\nPress Enter to continue...")


def print_start_menu():
    print("1. Continue Game")
    print("2. New Game")
    print("3. Records")
    print("4. Quit")


def ask_for_start_menu_choice():
    menu_choice = input("\nChoose an option (1-4): ").strip()
    while True:
        if menu_choice not in "1234":
            menu_choice = input("\nPlease Enter A Valid Choice (1-4): ").strip()
        else:
            return menu_choice


def print_stats(c):
    os.system("clear")
    print(c["name"])
    print("-------------------")
    print(c["art"])
    print("-------------------")
    print(f"HP: {c['max_hp']}")
    print(f"Physical Damage: {c['phy_dmg']}/33")
    print(f"Physical Defense: {c['phy_def']}/33")
    print(f"Magic Damage: {c['magic_dmg']}/33")
    print(f"Magic Defense: {c['magic_def']}/33")


def new_game():
    os.system("clear")
    print("Choose A Starting Class")
    print("-----------------------")
    print(f"1. {STARTING_CLASSES[0]['name']}")
    print(f"2. {STARTING_CLASSES[1]['name']}")
    print(f"3. {STARTING_CLASSES[2]['name']}")

    choice = (
        input("Choose a class to preview its stats (1-3, q to return): ")
        .strip()
        .lower()
    )
    while True:
        try:
            if choice != "q":
                print_stats(STARTING_CLASSES[int(choice) - 1])
                confirm = input("\nPress Enter to continue (q to return)")
                if confirm == "q":
                    return "", choice
                else:
                    return "Start", choice
            else:
                return "", choice
        except ValueError, IndexError:
            choice = (
                input("Please Enter A Valid Choice (1-3, q to return): ")
                .strip()
                .lower()
            )
