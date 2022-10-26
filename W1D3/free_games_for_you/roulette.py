import random
import time
class RouletteTicket:
    payouts = {
        'red': 2,
        'black': 2,
        'even': 2,
        'odd': 2,
        'one_to_18': 2,
        'nineteen_to_36': 2,
        'first_12': 3,
        'second_12': 3,
        'third_12': 3,
        'col_1': 3,
        'col_2': 3,
        'col_3': 3,
        'zero': 18,
        'dbl_zero': 18,
        'number': 18
    }
    bet_types = ['red',
        'black',
        'even',
        'odd',
        'one_to_18',
        'nineteen_to_36',
        'first_12',
        'second_12',
        'third_12',
        'col_1',
        'col_2',
        'col_3',
        'zero',
        'dbl_zero',
        'number']
    def __init__(self) -> None:
        self.bets = []


    def add_bet(self, bet):
        self.bets.append(bet)
        return self

    @staticmethod
    def determine_result(int):
        result = {'red':False, 'black':False, 'even':False, 'odd':False, 'one_to_18':False, 'nineteen_to_36':False, 'first_12':False, 
        'second_12':False, 'third_12':False, 'col_1':False, 'col_2':False, 'col_3': False, 'zero': False, 'dbl_zero': False, 'number': int}
        reds = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
        if int > 0 and int < 37:
            if int % 2:
                result['odd'] = True
            else: result['even'] = True
            if int in reds:
                result['red'] = True
            else:
                result['black'] = True
            if int % 3 == 0:
                result['col_3'] = True
            elif (int + 1) % 3 == 0:
                result['col_2'] = True
            else: result['col_1'] = True
            if int < 19:
                result['one_to_18'] = True
            else: result['nineteen_to_36'] = True
            if int < 13:
                result['first_12'] = True
            elif int < 25:
                result['second_12'] = True
            else: result['third_12'] = True
        else:
            if int == 37:
                result['zero'] = True
                result['number'] = "0"
            else: 
                result['dbl_zero'] = True
                result['number'] = "00"

        return result

class RouletteBet:
    def __init__(self, bet_type, amount, number=None) -> None:
        self.bet_type = bet_type
        self.amount = amount
        self.number = number

game = True
init = False
while(game):
    
    if not init:
        user_balance = 100
        my_ticket = RouletteTicket()
        init = True
        print(f"Welcome to Roulette!")

    print(f"Current Balance: {user_balance}")
    print("1. Make Bet")
    print("2. Cancel Bet")
    print(f"3. Review Bets ({len(my_ticket.bets)} set)")
    print("4. Spin")
    print("5. Show Payouts")
    print("6. Quit")

  
    choice = input("What will you do? \n>>")
    if choice == '6':
        print("Goodbye")
        game = False

    if choice == '1':
        if user_balance <= 0:
            print("Cannot afford more bets")
            continue
        i = 1
        print("Choose bet type:")
        for type in my_ticket.bet_types:
            print(f"{i} {type.capitalize()}")
            i+=1
        type_choice = input("\n>>")
        bet_type = my_ticket.bet_types[int(type_choice) -1]
        print(f"Bet chosen: {bet_type}")
        num = None
        if bet_type == 'number':
            while(num == None):
                temp_num = input("Choose a number between 1-36 \n>>")
                temp_num = int(temp_num)
                if temp_num < 1 or temp_num > 36:
                    print('Pick a valid number')
                else:
                    num = temp_num
        
        print(f"And how much will you wager? Current balance: {user_balance}")
        wager = 0
        while (wager == 0):
            temp_wage = int(input(">>"))

            if temp_wage > user_balance:
                print("Cannot afford bet")
            else:
                wager = temp_wage
        my_ticket.add_bet(RouletteBet(bet_type, wager, num))
        user_balance -= wager
    if choice == "2":
        i = 1
        for bet in my_ticket.bets:
            print(f"{i}) amount: {bet.amount} bet type: {bet.bet_type} ", end="", flush=True)
            if bet.number:
                print(f"({bet.number})")
            else: print("")
            i += 1
        if len(my_ticket.bets) == 0:
            print("No bets to cancel")
        else:
            cancelled = None
            while cancelled == None:
                print("Which bet to cancel? (Input number)")
                to_cancel = input(">>")
                if int(to_cancel) > len(my_ticket.bets) or int(to_cancel) <= 0:
                    print("Invalid choice")
                else:
                    cancelled = int(to_cancel)
            cancelled_wager = my_ticket.bets.pop(cancelled-1)
            user_balance += cancelled_wager.amount
    if choice == '3':
        print("Current bets:")
        for bet in my_ticket.bets:
            print(f"{bet.bet_type.capitalize()} ${bet.amount}", end="", flush= True)
            if bet.number:
                print(f" on {bet.number}")
            else: print("")
    if choice == "4":
        result = my_ticket.determine_result(random.randint(1,39))
        print("Spinning . ", end="", flush=True)
        for i in range(0,5):
            print(". ", end="", flush=True) 
            # time.sleep(0.5)
        print(f"Landed on {result['number']}", end="", flush=True)
        if result['red']:
            print(' (RED)')
        elif result['black']:
            print(' (BLACK)')
        else: print(' (GREEN)')
        wager_sum = 0
        result_sum = 0
        for bet in my_ticket.bets:
            win = False
            wager_sum += bet.amount
            if bet.bet_type == 'number':
                if result['number'] == bet.number:
                    win = True

            elif result[bet.bet_type]:
                win = True
            if win:
                winnings = bet.amount * RouletteTicket.payouts[bet.bet_type]
                print(f'Won bet type: {bet.bet_type.capitalize()} Wagered {bet.amount} received {winnings}', end="", flush=True)
                if bet.bet_type == 'number':
                    print(f' (bet on {bet.number})')
                else:
                    print("")
                result_sum += winnings
            else:
                print(f"Lost bet type: {bet.bet_type} Lost {bet.amount}" , end="", flush=True)
                if bet.bet_type == 'number':
                    print(f' (bet on {bet.number})')
                else:
                    print("")
        print(f"Total wager: {wager_sum}, Total payout: {result_sum}, win/loss: {result_sum - wager_sum}" )
        user_balance += result_sum
        print(f"New balance: {user_balance}")
        if user_balance <= 0:
            game = False
            print("You're broke, kid. Get outta here")
        else:   
            keep_on = input("Continue? Y/N \n>>")
            if keep_on.upper() == 'Y':
                my_ticket = RouletteTicket()
                continue
            else:
                game = False
                print("Adios!")
    if choice == "5":
        print("*"*30)
        for key in my_ticket.payouts:
            print(f"{key.capitalize()} pays {my_ticket.payouts[key] -1}:1")
        print("*"*30)
