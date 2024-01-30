from character import Character

class SuperCharacter(Character):
    def __init__(
        self,
        id = None,
        name = None,
        hit_points = 0,
        strength = 0,
        defense = 0
    ):
        self.special_used = False
        self.reinforcements_used = False

        Character.__init__(
            self,
            id=id,
            name=name,
            hit_points=hit_points,
            strength=strength,
            defense=defense
        )

        self.special = self.strength + 2
        self.reinforcements = 4
    
    def special_attack(self):
            self.special_used = True
            return Character().attack() + self.special
    
    def reinforcements_attack(self):
        self.reinforcements_used = True
        return self.reinforcements