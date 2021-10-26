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
    def process_input(cls, user_input, game_state_dict, instruction_number, default_message = 'Command not found, please re-enter. For a list of basic commands type `-help`.'):
        output = Helpers.recursive_lookup(user_input, game_state_dict, default_message)
        return output
        # # Check if output is a function (ie. sys.exit())
        # if hasattr(output, '__call__'): 
        #     return output()

        # if output == default_message:
        #     return cls.take_input(default_message)

        # # base case, return string
        # return cls.take_input(output)


        # update game state with choice
        # output next step in game

    @classmethod
    def process_next_step(cls, user_input, response_options):
        return Helpers.response_lookup(user_input, response_options)
        # take in game steps and process next prompt to be fed into take_input
        return ''


if __name__ == '__main__':
    Input_Ouput