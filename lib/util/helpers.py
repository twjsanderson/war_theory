
class Helpers:

    @staticmethod
    def string_to_list(str) -> list:
        list = str.split()
        return list
    
    @staticmethod
    def list_to_string(list) -> str:
        str = ' '.join(list)
        return str
    
    @staticmethod
    def string_to_lowercase(str) -> str:
        return str.lower()
