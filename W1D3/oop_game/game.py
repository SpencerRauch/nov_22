from game_classes.beggar import Beggar
from game_classes.mage import Mage
import random

player_1 = Beggar()
computer = Mage("Hagrid")

while player_1.health > 0 and computer.health > 0:
    response = ""
    while not response == "1" and not response == "2":
        print("Would you like 1) Attack or 2) Heal")
        response = input(">>>>")
        if response == "1":
            player_1.attack(computer)
        elif response == "2":
            player_1.heal()
        else:
            print("Please select a valid option")
        
    roll = random.randint(1,2)
    if roll == 1:
        computer.attack(player_1)
    else:
        computer.heal()

if player_1.health > 0:
    print("Congrats on kickin booty")
elif computer.health <= 0:
    print("It was a bloody draw")
else:
    print("Hagrid has pounded you into nothing")


    
