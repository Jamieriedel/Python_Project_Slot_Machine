import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6, 
    'D': 8}

symbol_value = { # rarity of symbols
    'A': 5,
    'B': 4,
    'C': 3, 
    'D': 2} 

def game(balance):
    lines = get_number_of_lines()
    while True: 
        bet = get_bet() 
        total_bet = bet * lines 
        if total_bet > balance:
            print(f"You don't have enough to bet that amount, your current balance is: ${balance}")
            continue
        else:
            break 

    print(f'You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}')

    # while True:
    #     checkpoint = input('Would you like to continue? [y/n] ')
    #     if checkpoint == 'y':
    #             break 
    #     elif checkpoint == 'n':
    #         # End the program
    #         print("Exiting the program.")
    #         exit()
    #     else:
    #         # Handle invalid input
    #         print("Invalid input. Please enter 'y' or 'n'.")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines) # * here is unpack or splat operator  

    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"current balance is ${balance}")
        answer = input("press enter to play (q to quit)")
        if answer == "q":
            break
        balance += game(balance) 

    print("You left with $", balance) 
    return balance  
    

def deposit():
    while True:
        amount = input('what would you like to deposit? $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else: 
                print('amount must be greater than 0.')
        else:
            print('please enter an number.')

    return amount


def get_number_of_lines():
    while True:
        lines = input('enter the number of lines to bet on (1-' + str(MAX_LINES) 
                      + ')? ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else: 
                print('enter a valid number of lines.')
                continue
        else:
            print('please enter an number.')
            continue
            
    return lines


def get_bet():
    while True:
        bet = input('please enter your bet: $')
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else: 
                print(f'amount must be between ${MIN_BET} and ${MAX_BET}.')
                continue
        else:
            print('please enter an number.')
            continue
    return bet


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = [] 
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count): # '_' is a invisible variable  
            all_symbols.append(symbol) 

    columns = [] 
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] # [:] basically is making a copy 
        for _ in range(rows):
            value = random.choice(all_symbols) 
            current_symbols.remove(value) 
            column.append(value) 
        columns.append(column)

    return columns 


def print_slot_machine(columns): # transpose rows to columns for a 3 x 3 picture
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], '|', end=" | ") # changes defauflt \n to sth. else
            else:
                print(column[row], end="") 
        print() # new row


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = [] 
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:                                 # if it doesn't break the for loop iteration will end with the else statement.
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines 


main() 