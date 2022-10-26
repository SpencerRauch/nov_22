#My original Hackathon from when I was a student!
import random
# Participants: Duy Pham, Nate Lunde, Spencer Rauch 
class Card:

    def __init__(self, suit, face):
        self.suit = suit
        self.face = face
    
        if self.face == 11:
            self.face = 'J'
        if self.face == 12:
            self.face = 'Q'
        if self.face == 13:
            self.face = 'K'
        if self.face == 14:
            self.face = 'A'

    def __repr__(self) -> str:
        return f'{self.face} of {self.suit}'

class Deck:

    def __init__(self):
        self.cards = []
        for i in range(2,15):
            self.cards.append(Card("diamonds", i))
        for i in range(2,15):
            self.cards.append(Card("hearts", i))
        for i in range(2,15):
            self.cards.append(Card("clubs", i))
        for i in range(2,15):
            self.cards.append(Card("spades", i))

    def deal(self):
        chosencard = random.choice(self.cards)
        self.cards.remove(chosencard)
        return chosencard

class BlackJackHand:
    def __init__(self, owner):
        self.owner = owner
        self.cards = []
    def addCard(self, card):
        self.cards.append(card)
        return self
    def evaluate(self):
        value = 0
        ace_count = 0
        for i in range (0,len(self.cards)):
            if type(self.cards[i].face) == int: 
                value += self.cards[i].face
            else:
                if self.cards[i].face != 'A':
                    value += 10
                else:
                    ace_count += 1
                    value += 11
        while value > 21 and ace_count > 0:
            value -= 10
            ace_count -= 1
        return value
    def __repr__(self) -> str:
        strmsg = f"{self.owner}'s Hand: \n"
        for card in self.cards:
            strmsg += f"{card} "
        return strmsg
        
# extra_ace = Card('hearts', 14) #for testing purposes
deck1 = Deck()
our_hand = BlackJackHand("Player").addCard(deck1.deal()).addCard(deck1.deal())
d_hand = BlackJackHand("Dealer").addCard(deck1.deal()).addCard(deck1.deal())

print(f'Our first card {our_hand.cards[0]}')
print(f'Our second card {our_hand.cards[1]}')
print(f'Count {our_hand.evaluate()}')

print(f"Dealer's first card {d_hand.cards[0]}")
# print(f"Dealer's second card {d_hand.cards[1]}")   #Comment lines 74 & 75 out to hide dealer's second card from the user
# print(f'Count {d_hand.evaluate()}')

if our_hand.evaluate() == 21 and d_hand.evaluate() != 21:
    print("BlackJACK!@#$@#$")

while our_hand.evaluate() < 21:
    #let player hit
    hit = input("Hit? Y/N")

    if hit.upper() == "Y":
        print("Hitting....")
        our_hand.addCard(deck1.deal())
        print(our_hand)
        print(f"Count {our_hand.evaluate()}")
    else:
        break

if our_hand.evaluate() > 21:
    print("Bust")

while d_hand.evaluate() < 17:
    d_hand.addCard(deck1.deal())

def endGame(msg):
    print(d_hand)
    print(d_hand.evaluate())
    print(msg)

if our_hand.evaluate() > d_hand.evaluate() and our_hand.evaluate() <= 21:
    endGame("Player wins!")

elif our_hand.evaluate() <= 21 and d_hand.evaluate() > 21:
    endGame("Player wins!")
elif our_hand.evaluate() == d_hand.evaluate():
    endGame("Push!")
else:
    endGame("Player loses")



