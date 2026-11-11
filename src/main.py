import os
from interface import menu, game, menu_stages, game_stages, round_stages, ROUNDS

os.system("clear")


def main():
    current_round = ROUNDS[0]
    print("Welcome To My CLI Project")
    while True:
        if not round_stages["round"]:
            player = menu()
            if player == "4":
                break
        else:
            current_round = game(player, current_round)


if __name__ == "__main__":
    main()
