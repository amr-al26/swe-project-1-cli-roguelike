import os

menu_stages = {"start_menu": True, "new_game": False}
game_stages = {"start_message": False, "tutorial": False}

ENEMIES = [
    {
        "name": "goblin",
        "hp": 50,
        "attack": {"name": "swipe", "dmg": 25, "type": "physical"},
        "phy_def": 10,
        "magic_def": 10,
    },
    {
        "name": "skeleton",
        "hp": 40,
        "attack": {"name": "bow shot", "dmg": 25, "type": "physical"},
        "phy_def": 5,
        "magic_def": 10,
    },
    {
        "name": "zombie",
        "hp": 75,
        "attack": {"name": "bite", "dmg": 30, "type": "physical"},
        "phy_def": 10,
        "magic_def": 5,
    },
    {
        "name": "ghost",
        "hp": 100,
        "attack": {"name": "haunt", "dmg": 25, "type": "magic"},
        "phy_def": 25,
        "magic_def": 10,
    },
    {
        "name": "witch",
        "hp": 60,
        "attack": {"name": "curse", "dmg": 35, "type": "magic"},
        "phy_def": 10,
        "magic_def": 30,
    },
    # Bosses
    {
        "name": "giant",
        "hp": 200,
        "attack": {"name": "slam", "dmg": 25, "type": "physical"},
        "phy_def": 20,
        "magic_def": 5,
    },
    {
        "name": "grim reaper",
        "hp": 125,
        "attack": {"name": "soul harvest", "dmg": 35, "type": "magic"},
        "phy_def": 10,
        "magic_def": 15,
    },
    {
        "name": "dragon",
        "hp": 150,
        "attack1": {"name": "fire breath", "dmg": 40, "type": "magic"},
        "attack2": {"name": "tail whip", "dmg": 40, "type": "physical"},
        "phy_def": 25,
        "magic_def": 25,
    },
]

STARTING_CLASSES = [
    {
        "name": "Wizard",
        "hp": 70,
        "phy_dmg": 5,
        "phy_def": 10,
        "magic_dmg": 16,
        "magic_def": 18,
    },
    {
        "name": "Magic Knight",
        "hp": 75,
        "phy_dmg": 10,
        "phy_def": 12,
        "magic_dmg": 10,
        "magic_def": 12,
    },
    {
        "name": "Warrior",
        "hp": 90,
        "phy_dmg": 16,
        "phy_def": 18,
        "magic_dmg": 5,
        "magic_def": 10,
    },
]

PHY_MOVES = [
    # Targets One
    {"name": "Kick", "dmg": 20, "target": "single"},
    {"name": "Headbutt", "dmg": 30, "target": "single"},
    {"name": "Bow Shot", "dmg": 40, "target": "single"},
    {"name": "Lunge", "dmg": 55, "target": "single"},
    {"name": "Giant Slash", "dmg": 70, "target": "single"},
    {"name": "Knockout", "dmg": 90, "target": "single"},
    # Targets All
    {"name": "Rampage", "dmg": 35, "target": "all"},
    {"name": "Rapid Slashes", "dmg": 55, "target": "all"},
]

MAGIC_MOVES = [
    # Targets One
    {"name": "Agi", "dmg": 20, "target": "single"},
    {"name": "Bufu", "dmg": 30, "target": "single"},
    {"name": "Zio", "dmg": 40, "target": "single"},
    {"name": "Garu", "dmg": 55, "target": "single"},
    {"name": "Psyo", "dmg": 70, "target": "single"},
    {"name": "Freila", "dmg": 90, "target": "single"},
    # Targets All
    {"name": "Maeiha", "dmg": 35, "target": "all"},
    {"name": "Megido", "dmg": 55, "target": "all"},
]

BUFFS = [
    {"name": "Tarukaja", "effect": "increase phy dmg"},
    {"name": "Makakaja", "effect": "increase magic dmg"},
]

STARTING_MOVE_SET = [
    {
        "name": "Wizard",
        "move_1": PHY_MOVES[0],
        "move_2": MAGIC_MOVES[2],
        "move_3": MAGIC_MOVES[6],
        "move_4": None,
    },
    {
        "name": "Magic Knight",
        "move_1": PHY_MOVES[0],
        "move_2": PHY_MOVES[6],
        "move_3": MAGIC_MOVES[0],
        "move_4": None,
    },
    {
        "name": "Warrior",
        "move_1": PHY_MOVES[2],
        "move_2": PHY_MOVES[6],
        "move_3": MAGIC_MOVES[0],
        "move_4": None,
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
                    return menu_choice
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

                if choice == "Start":
                    menu_stages["new_game"] = False
                    game_stages["start_message"] = True
                    running = False

                os.system("clear")

        if choice == "Start":
            break


def print_new_game_message():
    print("Welcome To The Beginning Of A New Journey Hero")
    input("\nPress Enter to continue...")
    print("You've Been Tasked With The Quest Of Slaying The Dragon")
    input("\nPress Enter to continue...")
    print("She Slumbers At The Other Side Of The Kingdom And Will Reek Havoc Upon Wake")
    input("\nPress Enter to continue...")
    print("You Will Face Countless Hardships On Your Journey But You Must Succeed")
    input("\nPress Enter to continue...")
    print("Farewell And Good Luck")


def game():
    if game_stages["start_message"]:
        print_new_game_message()
        game_stages["start_message"] = False


def game_menu():
    print("1. Attack")
    print("2. Defend")
    print("3. Check")
    print("4. Items")
    menu_choice = input("\nChoose an option (1-4): ").strip()


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
    print(f"HP: {c['hp']}")
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
                    break
                else:
                    return "Start"
            else:
                return choice
        except ValueError, IndexError:
            choice = (
                input("Choose a class to preview its stats (1-3, q to return): ")
                .strip()
                .lower()
            )
