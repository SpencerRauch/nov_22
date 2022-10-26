from game_classes.human import Human
# from game_classes import human

class Mage(Human):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.health = 50
        self.mana = 15

    def attack(self,target):
        # super().attack() use this if you want the parent version to run
        print(f"{self.name} is attacking {target.name}")
        target.defend(self.mana)

# mage1 = Mage("Albus")
# mage2 = Mage("Gandalf")

# mage1.attack(mage2)