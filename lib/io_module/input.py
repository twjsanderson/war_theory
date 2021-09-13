
class Input:
    
    @classmethod
    def take_user_input(cls, prompt = ''):
        user_input = ''
        if len(prompt) > 0:
            user_input = input(f'{prompt} ')
        else:
            user_input = input('')
        return user_input

    @classmethod
    def test(clas, arg):
        print(arg)
