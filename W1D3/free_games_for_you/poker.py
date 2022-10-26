import random, time

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

    def __repr__(self):
        strgmsg = ''
        for card in self.cards:
            strgmsg += f'{card}, '
        return strgmsg
        

class Card:

    def __init__(self, suit, face):
        self.suit = suit
        self.val = face
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
        return f"{self.face}_of_{self.suit}"
        
class PokerHand:
    hierarchy = {
        '10':'Royal Flush',
        '9': 'Straight Flush',
        '8': 'Four of A Kind',
        '7': 'Full House',
        '6': 'Flush',
        '5': 'Straight',
        '4': 'Three of A Kind',
        '3': 'Two Pair',
        '2': 'Pair',
        '1': 'High Card',
        '-1': 'Not 5 cards'
    }
    def __init__(self, owner) -> None:
        self.owner = owner
        self.cards = []
        self.is_straight = False
        self.is_flush = False
        self.suit_map = {
            'spades': 0,
            'diamonds': 0,
            'hearts': 0,
            'clubs': 0
        }

    def add_card(self, card):
        self.cards.append(card)
        key = card.suit
        self.suit_map[key] += 1;
        return self

    def remove_card(self, card):
        suit = card.suit
        self.cards.remove(card)
        self.suit_map[suit] -= 1;
        return self

    def is_full_hand(self):
        return len(self.cards) == 5

    def sort_cards_ace_as_14(self):
        self.cards.sort(key = self.fourteen_sort)
        return self

    def sort_cards_ace_as_1(self):
        self.cards.sort(key = self.one_sort)
        return self


    def check_straight(self):
        self.sort_cards_ace_as_1()
        flag = True
        for i in range(4):
            current_val = self.cards[i].val
            if current_val == 14:
                current_val = 1
            if not current_val == (self.cards[i+1].val - 1):
                flag = False
        if flag:
            self.is_straight = True
        self.sort_cards_ace_as_14()

        flag = True
        for i in range(4):
            card = self.cards[i]
            if not self.cards[i].val == (self.cards[i+1].val - 1):
                flag = False;
        if flag:
            self.is_straight = True

    def check_flush(self):
        for key in self.suit_map:
                if self.suit_map[key] == 5:
                    self.is_flush = True;
        return self
    def __repr__(self):
        string = ""
        count = 1
        for card in self.cards:
            string += str(count) + " - " + card.__repr__() + "\n"
            count += 1
        string += "Best hand: " + self.hierarchy[self.evaluate()]

        return string

    def evaluate(self):
        val = '-1'
        if self.is_full_hand():
            self.check_flush()
            self.check_straight()
            pairs = 0
            trip = False
            if self.is_straight and self.is_flush:
                val = '9'#straight flush
                if self.cards[4].val == 14:
                    val = '10'; #royal flush
                return val
            face_map = {}
            for card in self.cards:
                if card.face in face_map:
                    face_map[card.face] += 1
                else:
                    face_map[card.face] = 1
            for key in face_map:
                if face_map[key] == 4:
                    return '8' # four of a kind
                if face_map[key] == 3:
                    trip = True
                if face_map[key] == 2:
                    pairs += 1
                if trip and pairs == 1:
                    return '7' # full house
            if self.is_flush:
                return '6' # flush
            if self.is_straight:
                return '5' #straight
            if trip:
                return '4' #3 of a kind
            if pairs == 2:
                return '3' #two pair
            if pairs == 1:
                return '2' # one pair
            return '1' #High card


        return val 

    @staticmethod
    def fourteen_sort(card):
        return card.val

    @staticmethod
    def one_sort(card):
        if card.val == 14:
            return 1
        return card.val
# ace_spade = Card('spades', 14)
# king_spade = Card('spades', 10)
# queen_spade = Card('spades', 12)
# jack_spade = Card('spades', 13)
# ten_spade = Card('spades', 11)

# royalflush = PokerHand("Royal").add_card(ace_spade).add_card(king_spade).add_card(queen_spade).add_card(jack_spade).add_card(ten_spade);
# newdeck = Deck()
# newHand = PokerHand("Spencer");
# newHand.add_card(newdeck.deal()).add_card(newdeck.deal()).add_card(newdeck.deal()).add_card(newdeck.deal()).add_card(newdeck.deal())

# newHand.sort_cards_ace_as_1()
# print(newHand)
# newHand.sort_cards_ace_as_14()
# print(newHand)
# royalflush.sort_cards_ace_as_14()
# print(royalflush)

# royalflush.sort_cards_ace_as_1()
# print(royalflush)

payouts = {
    '10': 250,
    '9': 50,
    '8': 25,
    '7': 9,
    '6': 6,
    '5': 4,
    '4': 3,
    '3': 2,
    '2': 1,
    '1': 0,

}
player_balance = 100
print("Welcome To Terminal Poker! \nYou may exchange up to 4 cards one time")
print("*"*20)
print("Payout Table:")
for key in payouts:
    print(f"{PokerHand.hierarchy[key]}: x{payouts[key]}")
print("*"*20)


while(player_balance > 0):
    print(f"Your balance is {player_balance}")
    wager = 0
    wager = int(input("How much would you like to bet? \n >"))
    while(wager <= 0 or wager > player_balance):
        print(f"Invalid Wager: wager must fall in range: 0 < wager <= {player_balance}")
        wager = int(input("How much would you like to bet? \n >"))
    player_balance -= wager
    game_deck = Deck()
    player_hand = PokerHand("Player")
    player_hand.add_card(game_deck.deal()).add_card(game_deck.deal()).add_card(game_deck.deal()).add_card(game_deck.deal()).add_card(game_deck.deal())
    print("Initial hand:")
    print(player_hand.sort_cards_ace_as_14())
    draw = input("Would you like to draw? Y/N \n >")
    if draw.lower() == 'y':
        to_discard = -1
        while to_discard < 0 or to_discard > 4:
            to_discard = int(input("You may draw up 4 cards, how many would you like to draw? (0 to cancel draw) \n >"))
        to_draw = to_discard
        while to_discard > 0:
            print(f"{to_discard} cards to discard")
            print(player_hand)
            toRemove = int(input("Please specify card number to discard \n >")) -1
            if toRemove > len(player_hand.cards)-1 or toRemove < 0:
                print("Invalid card to remove")
                continue
            suit_to_update = player_hand.cards[toRemove].suit
            player_hand.suit_map[suit_to_update] -= 1
            player_hand.cards.pop(toRemove)
  
            to_discard -= 1
        while (to_draw > 0):
            print("Drawing a card....")
            time.sleep(0.5)
            player_hand.add_card(game_deck.deal())
            to_draw -= 1
        
    print(player_hand.sort_cards_ace_as_14())
    value = player_hand.evaluate()
    if int(value) > 1:
        multiplier = payouts[value]
        print(f"Paying out Wager x{multiplier} ({wager*multiplier}) for a {PokerHand.hierarchy[value]}")
        player_balance += wager * multiplier

    else:
        print(f"I'm sorry, no pay out. Wager lost (-{wager})")


print("I'm sorry, you're broke! Quitting")





    




