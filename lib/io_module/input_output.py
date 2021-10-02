from util.helpers import *

class Input_Ouput:
    string_to_lowercase = Helpers.string_to_lowercase

    @classmethod
    def take_input(cls, prompt = ''):
        user_input = ''

        if len(prompt) > 0:
            user_input = input(f'{prompt} ')
        else:
            user_input = input('')

        lower_case_user_input = cls.string_to_lowercase(user_input)

        return lower_case_user_input

    @classmethod
    def process_input(cls, user_input, game_state, default_message):
        return Helpers.recursive_lookup(user_input, game_state, default_message)
        # update game state with choice
        # output next step in game

    @classmethod
    def process_next_step():
        # take in game steps and process next prompt to be fed into take_input
        return ''


if __name__ == '__main__':
    Input_Ouput