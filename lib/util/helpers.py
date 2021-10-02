
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

    @classmethod
    def recursive_lookup(cls, input, dictionary, default_message = ''):
        if input in dictionary: 
            return dictionary[input]

        for value in dictionary.values():
            if isinstance(value, dict):
                response = cls.recursive_lookup(input, value)
                if response is not None: 
                    return response

        return default_message

if __name__ == '__main__':
    Helpers