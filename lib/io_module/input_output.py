from util.helpers import Helpers

class Input_Ouput:
    string_to_lowercase = Helpers.string_to_lowercase

    @classmethod
    def input_to_output(cls, prompt = '', instructions = None):
        user_input = ''
        if len(prompt) > 0:
            user_input = input(f'{prompt} ')
        else:
            user_input = input('')
        lower_case_user_input = cls.string_to_lowercase(user_input)

    @classmethod
    def process_user_input(cls, user_input, instructions):
        if isinstance(instructions, str):
            return instructions


