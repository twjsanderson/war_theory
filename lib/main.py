from sys import version
from constants import *
from io_module.input_output import *


def main():
    print(start_up_art)
    print(start_up_description)
    # for x in game_instructions:
    #     test = Input_Ouput.take_input(x)
    #     print(Input_Ouput.process_input(test, game_choice_dictiontary, 'Please re-enter your choice'))

    # This allows me to check if value is a function and then run it (ie. sys.exit()) 
    for x, v in game_choice_dictiontary.items():
        if hasattr(v, '__call__'):
            print('fdsaf')
            v()


    # li = { "thing": 3212}

    # for key, value in li.items():
    #     print(key, value)
    

if __name__ == '__main__':
    main()

