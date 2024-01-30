import random
import os
import time
from character import Character, SuperCharacter

class Main_Methods:
    def __init__(
        self,
        state,
        curr_step,
        curr_input
    ) -> None:
        self.state = state
        self.curr_step = curr_step
        self.curr_input = curr_input
        self.validations = self.curr_step['validations']
        self.character_ids = state['character_ids']
        self.hero = state['hero']
        self.companion = state['companion']
        self.monsters = state['monsters']
        self.path = state['path']

    def get_input(self):
        user_input = input('>>> ')
        self.validations = self.curr_step['validations']
        self.curr_input = user_input.lower()

        if self.validations != []:
            # all funcs need ot move to own class probs
            # change to oneliners
            def valid_len(input):
                length = len(input)
                if length > 0 and length < 10:
                    return True
                return False
            
            def is_one_to_five(input):
                if input in ['1','2','3','4','5']:
                    return True
                return False
        
            def yes_or_no(input):
                if input == 'y':
                    return True
                if input == 'n':
                    breakpoint()
                    # exit game
                    return
                return False

            def one_or_two(input):
                if input in ['1', '2']:
                    self.path = input
                    return True
                return False

            validation_rules = {
                'VALID_LEN': valid_len, 
                'IS_1_TO_5': is_one_to_five,
                'Y_OR_N': yes_or_no,
                '1_OR_2': one_or_two
            }

            for validation in self.validations:
                rule = validation_rules.get(validation)
                if rule is not None and rule(self.curr_input) is False:
                    print('Your input was invalid, please read the prompt carefully and try again.')
                    time.sleep(0.5)
                    self.get_input()
                elif rule is None or rule(self.curr_input) is True:
                    continue
        
        os.system('clear')

    def display_view(self):
        print(self.curr_step['view'])
    
    def __create_character_id(self):
        id = random.randint(0, 1000)
        if id in self.character_ids:
            self.__create_character_id()
        else:
            self.character_ids.append(id)
            return id
    
    def __build_character(self, name, hit_points, strength, defense, is_super=False):
        id = self.__create_character_id()
        if is_super:
            return SuperCharacter(id, name, hit_points, strength, defense)
        else:
            return Character(id, name, hit_points, strength, defense)
    
    def create_hero(self):
        self.hero = self.__build_character(self.curr_input, 4, 4, 4, True)
    
    def set_hero_name(self):
        self.hero.name = self.curr_input
    
    def display_view_with_hero_name(self):
        print(self.curr_step['view'].format(name=self.hero.get_name()))
    
    def create_companion(self):
        companion = {
            '1': self.__build_character('Thrack', 2, 2, 2),
            '2': self.__build_character('Quill', 4, 1, 1),
            '3': self.__build_character('Rafe', 3, 1, 2),
            '4': self.__build_character('Cathos', 1, 4, 1),
            '5': self.__build_character('Selwyn', 2, 1, 3)
        }
        self.companion = companion[self.curr_input]
    
    def display_view_with_companion_name(self):
        print(self.curr_step['view'].format(name=self.companion.get_name()))

if __name__ == '__main__':
    Main_Methods