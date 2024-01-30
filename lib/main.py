from art import *
from engine import Game_Engine
from state import *

class Main:
    def __init__(self):
        self.game_engine = Game_Engine(state)
    
    def show_start_up(self):
        els = [start_up_art, start_up_description]
        for el in els:
            print(el)
    
    def init_game(self):
        self.show_start_up() # move to game_engine so we can call it on line 32
        input('>>> ')
        self.game_engine.process_actions()
        self.game_engine.process_next_step()

if __name__ == '__main__':
    Main().init_game()
