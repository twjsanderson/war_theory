from constants import *
from game_module.game import Game


def main():
    # prints out start up art & description
    print(start_up_art)
    print(start_up_description)

    Game.intro_1()

if __name__ == '__main__':
    main()

