# Imports
import random

# Constants
MAX_LINES = 3
MAX_BET = 1000000
MIN_BET = 1

ROWS = 3
COLS = 3


# amount of each symbol in one col i think
symbol_count = {
    "#": 2,
    "7": 4,
    "$": 6,
    "/": 8
}
symbol_value = {
    "#": 5,
    "7": 4,
    "$": 3,
    "/": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []

    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines







def get_slot_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():  #loops through for char, and its occurence, if symbol = "A", then count = 2
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = [] # define columns list
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] # creates a copy list to make sure no changes are made to all_symbols
        for _ in range(rows):   # generates number of values that need to be generated, hence "range(rows)"
            value = random.choice(current_symbols)
            current_symbols.remove(value) # removes a value that has already been used, If A picked then there will be 1 A instead of 2 etc.
            column.append(value)
    # all code above picks a random value for each row in each column
        columns.append(column)
    return columns


def print_slots(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()



def deposit():
    while True:
        amount = input("Enter deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero")
        else:
            print("Please enter a number.")
    return amount

def number_of_lines():
    while True:
        lines = input("# of lines to bet on (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Lines must be between 1 and 3")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        amount = input("Enter bet for each line: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number.")
    return amount

def spin(balance):
    lines = number_of_lines()
    while True:
        bet = get_bet()
        print()
        total_bet = bet * lines
        if balance >= total_bet:
            break
        else:
            print(f"Your balance is too low!\nYour balance: ${balance}\n")
    print(f"You are betting ${bet} on {lines} lines. Total bet: ${total_bet}")

    slots = get_slot_spin(ROWS, COLS, symbol_count)
    print_slots(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on line", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to spin (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")





main()


