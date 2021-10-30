from game_state import *
from art import *
from game_module.game import Game
# from character_module.character import Character


def main():
    # prints out start up art & description
    print(start_up_art)
    print(start_up_description)

    Game.run_game(1)
    # player = Character('tom')

    # player.show_name()

if __name__ == '__main__':
    main()

