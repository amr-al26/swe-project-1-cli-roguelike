import os
from interface import menu, game, menu_stages, game_stages

os.system("clear")


def main():
    print("Welcome To My CLI Project")
    while True:
        if not game_stages["start"]:
            menu()
        else:
            game()


if __name__ == "__main__":
    main()
