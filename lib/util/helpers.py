
class Helpers:

    @staticmethod
    def string_to_list(str):
        list = str.split()
        return list
    
    @staticmethod
    def list_to_string(list):
        str = ' '.join(list)
        return str

helper = Helpers
print(helper.string_to_list('fgjds khfj'))
print(helper.list_to_string(['fgjds', 'khfj']))