import os
from interface import menu, game, menu_stages, game_stages, round_stages, ROUNDS

os.system("clear")


def main():
    current_round = ROUNDS[0]
    print("Welcome To My CLI Project")
    while True:
        if not round_stages["round"]:
            menu_choice = menu()
            if menu_choice == "4":
                break
        else:
            current_round = game(menu_choice, current_round)


if __name__ == "__main__":
    main()
