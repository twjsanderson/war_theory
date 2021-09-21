from util.helpers import Helpers

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
    def process_input(cls, user_input, game_state, output):
        # take user input in response to question
        # update game state with choice
        # output next step in game
        return 

    @classmethod
    def process_next_step():
        # take in game steps and process next prompt to be fed into take_input
    


