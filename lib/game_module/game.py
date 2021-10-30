import time
from game_state import *
from character_module.character import *

class Game:
    levels_that_require_text_input = [3, 7]
    levels_that_show_character_information = [4]

    @classmethod
    def run_game(cls, game_level):

        # if game_level not in cls.levels_that_show_character_information:
        #     print(game_state[game_level]['story_point'])
        #     user_input = input('>>> ')
        #     time.sleep(1)

        if game_level in cls.levels_that_show_character_information:
            if game_level == 4:
                player = game_state['player']
                name = player.show_name() 
                print(game_state[game_level]['story_point'].format(name))
                user_input = input('>>> ')
                time.sleep(1)
            
            # call run_game again with the next story point
            return cls.run_game(game_state[game_level]['responses'][game_level + 1])
        
        if len(user_input) > 0 and game_level in cls.levels_that_require_text_input:
            if game_level == 3:
                newPlayer = Character()
                newPlayer.update_name(user_input)
                game_state['player'] = newPlayer
                # call run_game again with the next story point
                return cls.run_game(game_state[game_level]['responses'][game_level + 1])
            
        
        if user_input in game_state[game_level]['responses']:
            # if response value is a function excute it
            if hasattr(game_state[game_level]['responses'][user_input], '__call__'): 
                return game_state[game_level]['responses'][user_input]()
            
            # call run_game again with the next story point
            return cls.run_game(game_state[game_level]['responses'][user_input])
        
        # if user input not found in responses dict
        return cls.run_default(game_level, user_input)

    @classmethod
    def run_default(cls, game_level, user_input):
        if user_input in game_state['default']:

            # if response value is a function excute it
            if hasattr(game_state['default'][user_input], '__call__'): 
                return game_state['default'][user_input]()
            
            print(game_state['default'][user_input])
            user_input = input('>>> ')
            if user_input == '':
                cls.run_game(game_level)
            return cls.run_default(game_level, user_input)

        print('''
        *** Input not understood, Please re-read the game prompt again or enter -help for a list of valid commands ***
        ''')
        user_input = input('>>> Hit enter to continue')
        if user_input == '':
            cls.run_game(game_level)
        return cls.run_default(game_level, user_input)

if __name__ == '__main__':
    Game