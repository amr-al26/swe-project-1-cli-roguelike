import os
from data import *
from calculations import attack, enemy_attack, healing
from itertools import zip_longest

menu_stages = {"start_menu": True, "new_game": False, "records": False}
game_stages = {"start_message": False, "tutorial": False}
round_stages = {
    "round": False,
    "intro_message": False,
    "menu_selection": False,
    "action_summary": False,
    "enemies_turn": False,
    "upgrades": False,
    "end_screen": False,
}

player = {}
inventory = [dict(ITEMS[0])]


def menu():
    while True:
        msg = ""
        if menu_stages["start_menu"]:
            print_start_menu()
            menu_choice = input("\nChoose an option (1-3): ").strip()
            running = True
            while running:
                if menu_choice == "1":
                    menu_stages["start_menu"] = False
                    menu_stages["new_game"] = True
                    running = False
                elif menu_choice == "2":
                    menu_stages["start_menu"] = False
                    menu_stages["records"] = True
                    running = False
                elif menu_choice == "3":
                    return menu_choice
                else:
                    menu_choice = input("\nPlease Enter A Valid Choice (1-3): ").strip()

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

        if menu_stages["records"]:
            if len(runs) > 0:
                for run in runs:
                    print_run_data(run)
                    print("\n" * 3)
            else:
                print("No Records Available")

            input("Press Enter to continue...")
            os.system("clear")

            menu_stages["records"] = False
            menu_stages["start_menu"] = True


def print_run_data(player):
    print(f"Name: {player['name']}")
    print(f"Class: {player['class_name']}")
    print("------------------------------")
    print("Stats")
    print("------------------------------")
    print(f"Max HP: {player['max_hp']}")
    print(f"Physical Damage: {player['phy_dmg']}/33")
    print(f"Physical Defense: {player['phy_def']}/33")
    print(f"Magic Damage: {player['magic_dmg']}/33")
    print(f"Magic Defense: {player['magic_def']}/33")

    print_move_set(player["move_set"])

    print("------------------------------")
    print(f"Status: {player['status']}")


def print_new_game_message(player):
    name = input("What Is Your Name Adventurer?: ")
    while True:
        if name.strip() != "":
            break
        name = input("Please Enter A Valid Name: ")

    player["name"] = name
    input("\nPress Enter to continue...")
    os.system("clear")
    print(f"Welcome To The Beginning Of A New Journey {name}")
    input("\nPress Enter to continue...")
    os.system("clear")
    print(f"Welcome To The Beginning Of A New Journey {name}")
    print("You've Been Tasked With The Quest Of Slaying The Dragon")
    input("\nPress Enter to continue...")
    os.system("clear")
    print(f"Welcome To The Beginning Of A New Journey {name}")
    print("You've Been Tasked With The Quest Of Slaying The Dragon")
    print("She Slumbers At The Other Side Of The Kingdom And Will Reek Havoc Upon Wake")
    input("\nPress Enter to continue...")
    os.system("clear")
    print(f"Welcome To The Beginning Of A New Journey {name}")
    print("You've Been Tasked With The Quest Of Slaying The Dragon")
    print("She Slumbers At The Other Side Of The Kingdom And Will Reek Havoc Upon Wake")
    print("You Will Face Countless Hardships On Your Journey But You Must Succeed")
    input("\nPress Enter to continue...")
    os.system("clear")
    print(f"Welcome To The Beginning Of A New Journey {name}")
    print("You've Been Tasked With The Quest Of Slaying The Dragon")
    print("She Slumbers At The Other Side Of The Kingdom And Will Reek Havoc Upon Wake")
    print("You Will Face Countless Hardships On Your Journey But You Must Succeed")
    print("Farewell And Good Luck")
    input("\nPress Enter to continue...")


def game(player, round):
    if game_stages["start_message"]:
        print_new_game_message(player)
        os.system("clear")
        game_stages["start_message"] = False
        round_stages["intro_message"] = True

    if round_stages["round"]:
        return game_interface(player, round)


def print_move_set(move_set):
    print("-----------------")
    print("Move Set")
    print("-----------------")
    for index, move in enumerate(move_set):
        print(
            f"{index + 1}. {move['name']} Damage: {move['dmg']} Type: {'Physical' if move in PHY_MOVES else 'Magic'} Target: {move['target']}"
        )


def move_selection(move_set):

    print_move_set(move_set)

    move = input("\nChoose an option (1-4, q to return): ").strip()

    while True:
        try:
            if move.lower() == "q":
                return "return"

            return move_set[int(move) - 1]
        except ValueError, IndexError:
            move = input("\nPlease Enter A Valid Choice (1-4, q to return): ").strip()


def target_selection(round):
    print("-----------------")
    print("Opponent(s)")
    print("-----------------")
    index = 0
    for enemy in round["enemies"]:
        print(f"{index + 1}. {enemy['name']}")
        index += 1

    choice = input(f"\nChoose an option (1-{index}, q to return): ").strip()
    while True:
        if choice.lower() == "q":
            return "return", None

        if choice.isdigit():
            if 0 < int(choice) <= index:
                return round["enemies"][int(choice) - 1], int(choice) - 1

        choice = input(
            f"\nPlease Enter A Valid Choice (1-{index}, q to return): "
        ).strip()


def print_game_menu(player, round):
    print(
        side_by_side(player["art"], *[enemies["art"] for enemies in round["enemies"]])
    )
    enemies_hp = ""
    for enemies in round["enemies"]:
        enemies_hp += f"| {enemies['name']}: {enemies['hp']} HP "

    print(f"-----------------{'-' * len(enemies_hp)}")
    print(f"HP: {player['hp']}/{player['max_hp']}{' ' * 7}{enemies_hp}")
    print(f"-----------------{'-' * len(enemies_hp)}")


def print_inventory(inventory):
    print("-----------------")
    print("Inventory")
    print("-----------------")
    if len(inventory) == 0:
        print("Your Inventory Is Empty.")
        return "return"
    index = 0
    for item in inventory:
        print(
            f"{index + 1}. {item['name']} (Level {item['lvl']}): Heals {item['healing']} HP"
        )
        index += 1

    choice = input(f"\nChoose an option (1-{index}, q to return): ").strip()
    while True:
        if choice.lower() == "q":
            return "return"

        if choice.isdigit():
            if 0 < int(choice) <= index:
                return inventory[int(choice) - 1]

        choice = input(
            f"\nPlease Enter A Valid Choice (1-{index}, q to return): "
        ).strip()


def print_enemies_stats(round):
    for enemy in round["enemies"]:
        print("-----------------")
        print(enemy["name"])
        print("-----------------")
        print(f"Physical Defense: {enemy['phy_def']}/33")
        print(f"Magic Defense: {enemy['magic_def']}/33")


def upgrades(c, points):

    while points > 0:
        print(c["art"])
        print("-------------------")
        print(f"1. HP: {c['hp']}/{c['max_hp']}")
        print(f"2. Physical Damage: {c['phy_dmg']}/33")
        print(f"3. Physical Defense: {c['phy_def']}/33")
        print(f"4. Magic Damage: {c['magic_dmg']}/33")
        print(f"5. Magic Defense: {c['magic_def']}/33")

        print(f"\n{points} Upgrade{'s' if points > 1 else ''} Remaining")
        choice = input("\nChoose a stat to upgrade(1-5): ").strip()

        while True:
            if choice == "1":
                c["hp"] += 5
                c["max_hp"] += 5
                points -= 1
                break
            elif choice == "2":
                if c["phy_dmg"] == 33:
                    print("This Stat Is Maxed Out")
                    input("Press Enter To Continue...")
                    break
                c["phy_dmg"] += 1
                points -= 1
                break
            elif choice == "3":
                if c["phy_def"] == 33:
                    print("This Stat Is Maxed Out")
                    input("Press Enter To Continue...")
                    break
                c["phy_def"] += 1
                points -= 1
                break
            elif choice == "4":
                if c["magic_dmg"] == 33:
                    print("This Stat Is Maxed Out")
                    input("Press Enter To Continue...")
                    break
                c["magic_dmg"] += 1
                points -= 1
                break
            elif choice == "5":
                if c["magic_def"] == 33:
                    print("This Stat Is Maxed Out")
                    input("Press Enter To Continue...")
                    break
                c["magic_def"] += 1
                points -= 1
                break
            else:
                choice = input("\nPlease Enter A Valid Choice(1-5): ").strip()

        os.system("clear")

    print(c["art"])
    print("-------------------")
    print(f"1. HP: {c['hp']}/{c['max_hp']}")
    print(f"2. Physical Damage: {c['phy_dmg']}/33")
    print(f"3. Physical Defense: {c['phy_def']}/33")
    print(f"4. Magic Damage: {c['magic_dmg']}/33")
    print(f"5. Magic Defense: {c['magic_def']}/33")
    input("\nPress Enter To Continue...\n")


def move_addition(player, new_moves):
    print("You Unlocked A New Move!")
    print_move_set(player["move_set"])
    print("-----------------")
    print("New Moves")
    for index, move in enumerate(new_moves):
        print(
            f"{index + 1}. {move['name']} Damage: {move['dmg']} Type: {'Physical' if move in PHY_MOVES else 'Magic'} Target: {move['target']}"
        )

    choice = input("Pick A Move (1-2, q to skip): ").strip()
    while True:
        if choice == "1" or choice == "2":
            break

        if choice.lower() == "q":
            return

        choice = input("Please Enter A Valid Choice (1-2, q to skip): ").strip()

    if len(player["move_set"]) == 4:
        replacement = input(
            "You have the maximum amount of moves, select a move to replace (1-4): "
        )
        try:
            player["move_set"][int(replacement) - 1] = new_moves[int(choice) - 1]
        except ValueError, IndexError:
            replacement = input("Please Enter A Valid Choice (1-4): ")
    else:
        player["move_set"].append(new_moves[int(choice) - 1])

    input("\nPress Enter To Continue...")


def check_for_round_end(round):
    return len(round["enemies"]) == 0


def game_interface(player, round):
    while round_stages["intro_message"]:
        print(
            side_by_side(
                player["art"], *[enemies["art"] for enemies in round["enemies"]]
            )
        )
        print("-----------------")
        print(f"HP: {player['hp']}/{player['max_hp']}")
        print("-----------------")
        print("A Horde Of Enemies Approach")
        input("\nPress Enter To Continue...")
        round_stages["intro_message"] = False
        round_stages["menu_selection"] = True
        os.system("clear")

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
                inventory.pop(inventory.index(item))
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
            if move["target"] == "all":
                for enemy in round["enemies"][:]:
                    dmg, status = attack(player, enemy, move)
                    print(f"{move['name']} dealt {dmg} damage to {enemy['name']}!")
                    if status == "dead":
                        print(f"{enemy['name']} has fallen!")
                        round["enemies"].remove(enemy)

                    print()
            else:
                dmg, status = attack(player, target, move)
                os.system("clear")
                print_game_menu(player, round)
                print(f"{move['name']} dealt {dmg} damage to {target['name']}!")
                if status == "dead":
                    print(f"{target['name']} has fallen!")
                    round["enemies"].pop(index)

            if check_for_round_end(round) and round["index"] != 10:
                print(
                    f"You earned {round['rewards']['points']} points and a Level {round['rewards']['items']['lvl']} {round['rewards']['items']['name']}!"
                )
                inventory.append(dict(round["rewards"]["items"]))
                round_stages["action_summary"] = False
                round_stages["upgrades"] = True
                input("\nPress Enter to continue...")
                os.system("clear")
                return ROUNDS[round["index"]] if round["index"] != 10 else None
            elif check_for_round_end(round):
                player["status"] = "Completed Run"
                print("\nCongratulations On Beating The Game!!")
                input("Press Enter To View The Game Summary...")
                os.system("clear")
                print("Game Summary")
                print("------------------------------")
                round_stages["end_screen"] = True
                round_stages["action_summary"] = False
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
        enemy_attack_msg = ""
        for enemy in round["enemies"]:
            dmg, move = enemy_attack(enemy, player, defend)
            print_game_menu(player, round)
            enemy_attack_msg += f"{enemy['name']} uses {move['name']} ({move['type'].title()}) and does {dmg} dmg\n"
            print(enemy_attack_msg)

            if player["hp"] == 0:
                player["dead"] = True
                player["status"] = (
                    f"Failed Run (Died At Round {round['index']} to {enemy['name']})"
                )
                print("\033[0;31mYOU DIED\033[0m")
                input("Press Enter To View The Game Summary...\n")
                os.system("clear")
                round_stages["end_screen"] = True
                break

            input("Press Enter To Continue...\n")
            os.system("clear")

        if not round_stages["end_screen"]:
            round_stages["enemies_turn"] = False
            round_stages["menu_selection"] = True
        else:
            round_stages["enemies_turn"] = False

    while round_stages["upgrades"]:
        upgrades(player, ROUNDS[round["index"] - 2]["rewards"]["points"])
        if "moves" in ROUNDS[round["index"] - 2]["rewards"]:
            move_addition(player, ROUNDS[round["index"] - 2]["rewards"]["moves"])
        round_stages["upgrades"] = False
        round_stages["intro_message"] = True
        os.system("clear")

    while round_stages["end_screen"]:
        print_run_data(player)
        runs.append(player)
        input("\nPress Enter To Return To The Main Menu...")
        os.system("clear")

        menu_stages["start_menu"] = True
        round_stages["round"] = False
        round_stages["end_screen"] = False

    return round


def side_by_side(*arts, gap=10):
    blocks = [a.splitlines() for a in arts]
    n = max(map(len, blocks))
    blocks = [[""] * (n - len(b)) + b for b in blocks]
    widths = [max(map(len, b)) for b in blocks]
    return "\n".join(
        (" " * gap).join(line.ljust(w) for line, w in zip(row, widths)).rstrip()
        for row in zip(*blocks)
    )


def print_start_menu():
    print("1. New Game")
    print("2. Records")
    print("3. Quit")


def ask_for_start_menu_choice():
    menu_choice = input("\nChoose an option (1-3): ").strip()
    while True:
        if menu_choice not in "123":
            menu_choice = input("\nPlease Enter A Valid Choice (1-4): ").strip()
        else:
            return menu_choice


def print_stats(player):
    os.system("clear")
    print(player["class_name"])
    print("-------------------")
    print(player["art"])
    print("-------------------")
    print(f"HP: {player['max_hp']}")
    print(f"Physical Damage: {player['phy_dmg']}/33")
    print(f"Physical Defense: {player['phy_def']}/33")
    print(f"Magic Damage: {player['magic_dmg']}/33")
    print(f"Magic Defense: {player['magic_def']}/33")

    print_move_set(player["move_set"])


def new_game():
    os.system("clear")
    print("Choose A Starting Class")
    print("-----------------------")
    print(f"1. {STARTING_CLASSES[0]['class_name']}")
    print(f"2. {STARTING_CLASSES[1]['class_name']}")
    print(f"3. {STARTING_CLASSES[2]['class_name']}")

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
