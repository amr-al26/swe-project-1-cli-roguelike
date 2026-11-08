import os

menu_stages = {"start_menu": True, "new_game": False}

STARTING_CLASSES = [
    {
        "name": "Wizard",
        "hp": 65,
        "mana": 60,
        "phy_dmg": 0.25,
        "phy_def": 0.25,
        "magic_dmg": 0.60,
        "magic_def": 0.70,
        "evasion": 0.20,
    },
    {
        "name": "Magic Knight",
        "hp": 75,
        "mana": 45,
        "phy_dmg": 0.45,
        "phy_def": 0.45,
        "magic_dmg": 0.50,
        "magic_def": 0.60,
        "evasion": 0.30,
    },
    {
        "name": "Warrior",
        "hp": 90,
        "mana": 25,
        "phy_dmg": 0.60,
        "phy_def": 0.60,
        "magic_dmg": 0.25,
        "magic_def": 0.25,
        "evasion": 0.40,
    },
]

PHY_MOVES = [
    # Targets One
    {"name": "Kick", "dmg": "low", "target": "single"},
    {"name": "Headbutt", "dmg": "med", "target": "single"},
    {"name": "Bow Shot", "dmg": "med", "target": "single"},
    {"name": "Lunge", "dmg": "med", "target": "single"},
    {"name": "Giant Slash", "dmg": "high", "target": "single"},
    {"name": "Knockout", "dmg": "high", "target": "single"},
    # Targets All
    {"name": "Rampage", "dmg": "low", "target": "all"},
    {"name": "Rapid Slashes", "dmg": "med", "target": "all"},
]

MAGIC_MOVES = [
    # Targets One
    {"name": "Agi", "dmg": "low", "target": "single"},
    {"name": "Bufu", "dmg": "low", "target": "single"},
    {"name": "Zio", "dmg": "low", "target": "single"},
    {"name": "Garu", "dmg": "low", "target": "single"},
    {"name": "Psyo", "dmg": "med", "target": "single"},
    {"name": "Freila", "dmg": "med", "target": "single"},
    # Targets All
    {"name": "Maeiha", "dmg": "low", "target": "all"},
    {"name": "Megido", "dmg": "med", "target": "all"},
]

BUFFS = [
    {"name": "Tarukaja", "effect": "increase phy dmg"},
    {"name": "Makakaja", "effect": "increase magic dmg"},
]

STARTING_MOVE_SET = [
    {
        "name": "Wizard",
        "move_1": PHY_MOVES[0],
        "move_2": MAGIC_MOVES[0],
        "move_3": MAGIC_MOVES[1],
        "move_4": MAGIC_MOVES[6],
    },
    {
        "name": "Magic Knight",
        "move_1": PHY_MOVES[0],
        "move_2": PHY_MOVES[1],
        "move_3": MAGIC_MOVES[2],
        "move_4": MAGIC_MOVES[4],
    },
    {
        "name": "Warrior",
        "move_1": PHY_MOVES[0],
        "move_2": PHY_MOVES[2],
        "move_3": PHY_MOVES[4],
        "move_4": PHY_MOVES[6],
    },
]


def menu():
    while True:
        if menu_stages["start_menu"]:
            running = True
            while running:
                print_start_menu()

                menu_choice = input("\nChoose an option (1-4): ").strip()

                if menu_choice == "1":
                    print("No Current Save Available")
                elif menu_choice == "2":
                    menu_stages["start_menu"] = False
                    menu_stages["new_game"] = True
                    running = False
                elif menu_choice == "3":
                    pass
                elif menu_choice == "4":
                    return
                else:
                    menu_choice = input("\nPlease Enter A Valid Choice (1-4): ").strip()

                input("\nPress Enter to continue...")
                os.system("clear")

        if menu_stages["new_game"]:
            running = True
            while running:
                choice = new_game()
                if choice == "q":
                    menu_stages["start_menu"] = True
                    menu_stages["new_game"] = False
                    running = False
                os.system("clear")


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
    print(f"HP: {c['hp']}")
    print(f"Mana: {c['mana']}")
    print(f"Physical Damage: {c['phy_dmg']}")
    print(f"Physical Defense: {c['phy_def']}")
    print(f"Magic Damage: {c['magic_dmg']}")
    print(f"Magic Defense: {c['magic_def']}")
    print(f"Evasion: {c['evasion']}")


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
                input("\nPress Enter to continue...")
                break
            else:
                return choice
        except ValueError, IndexError:
            choice = (
                input("Choose a class to preview its stats (1-3, q to return): ")
                .strip()
                .lower()
            )
