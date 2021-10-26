import time 
from constants import *

class Game:
    one = ['']

    @classmethod
    def intro_1(cls):
        print(story[1])
        time.sleep(1)
        user_input = input('>>> ')
        if user_input in cls.one:
            return cls.intro_2()

    @classmethod
    def intro_2(cls):
        print(story[2])
        time.sleep(1)
        user_input = input('>>> ')
        #if user_input .length > 0 and less than 15
        # add to state
    



if __name__ == '__main__':
    Game