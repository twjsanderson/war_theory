class Character:
    def __init__(
        self,
        id,
        name = None,
        hit_points = 0,
        strength = 0,
        defense = 0
    ):  
        self.id = id
        self.name = self.__set_name(name)
        self.hit_points = hit_points
        self.strength = strength
        self.defense = defense

    def get_id(self):
        return self.id
    
    def __set_name(self, name):
        return name.capitalize()

    def get_name(self):
        return self.name

    def attack(self):
        return self.strength

    def defend(self, attack):
        if attack >= self.defense + self.hit_points:
            self.hit_points = 0
        if (
            attack < self.defense + self.hit_points and
            attack > self.defense
        ):
            attack -= self.defense
            self.hit_points -= attack
    
    def check_health(self):
        return self.hit_points

if __name__ == '__main__':
    Character
