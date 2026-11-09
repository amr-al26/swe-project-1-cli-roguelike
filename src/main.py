import os
from interface import menu, game, menu_stages, game_stages

os.system("clear")


def main():
    print("Welcome To My CLI Project")
    while True:
        if not game_stages["start_message"]:
            menu_choice = menu()
            if menu_choice == "4":
                break
        else:
            game()


if __name__ == "__main__":
    main()
