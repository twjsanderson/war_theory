
from methods import Battle_Methods
from methods import Main_Methods

class Game_Engine(Main_Methods, Battle_Methods):
    def __init__(self, state):
        self.state = state
        self.story = state['story']
        self.step = 0
        self.curr_step = state['story'][self.step]
        self.curr_input = ''
        
        Main_Methods.__init__(
            self,
            state=state,
            curr_step=self.curr_step,
            curr_input=self.curr_input
        )

        Battle_Methods.__init__(
            self,
            state=state,
            curr_step=self.curr_step,
            curr_input=self.curr_input
        )

    def process_next_step(self):
        if self.step == len(self.story) - 1:
            print('end of game')
            breakpoint()
            return
        self.step += 1
        self.curr_step = self.story[self.step]
        self.process_actions()
        self.process_next_step()

    def process_actions(self):
        # execute methods from all classes
        for action in self.curr_step['actions']:
            # check if action in self.curr_step['validation']
            # if yes, pass in validation list below
            getattr(
                super(),
                action.lower()
            )()
        self.curr_input = ''

if __name__ == '__main__':
    Game_Engine
