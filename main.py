import random

# Global constant
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

#Symbols
"""
Each reel has...
A - represents most valueable
then going to the lowest.
"""

symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_slot_machine_spin(rows, cols, symbols):

    """
    For example
    - In symbol count "A" is symbol and its symbol_count
    will return 2. Symbols.items() will look for items in the list.
    For loop loops through the symbol_count and then stores it in
    all_symbols.

    Instead of putting i put _ is inserted because its an annoymous variable
    that doesn't care about the count and then you't don't have
    an unused variable.
    """

    all_symbols = []
    for symbol, symbol_count, in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    # Here we select what values go in every single column.
    # Here each nested list represents values of the column.

    columns = []
    # For every column we must generate a certain number of symbols.
    # Generated a column for every single column that is present.
    for _ in range(cols):
        column = []
        # Making a copy instead of using all_symbols because it will include values removed.
        current_symbols = all_symbols[:] # <- Copies list ":"
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value) # <- Finds first instance of values of the list and removes it so it's not picked again.
            column.append(value) # <- Add values to our column

        columns.append(column) # <- Add columns to columns list.

    return columns

def print_slot_machine(columns):
    
    """
    Need to determine the number of rows based on the columns
    which is the number of elements in each columns.
    - Enumerate gives the index as well as the item.
    - len(columns) - 1 is the maximum index we have to access an element in the columns list.
    """

    for row in range(len(columns[0])):
        # Print value that is at the first row of that column
        # loop through every single row
        for i, column in enumerate(columns):
            # For every row we loop through every column
            if i != len(columns) - 1:
                print(column[row], "|")
            else:
                print(column[row])


def deposit():

    """
    isdigit() tells if its a valid whole number. Since its a string we need
    a numeric value for deposit balance. The amount has to be greater than 0.
    If so the function stops but it its less than 0 it returns a print statement.
    The second else returns a print statement stating it must be a number.
    """

    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number on lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines

def get_bet():
    while True:
        amount = input("How much would you like to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()

    # Can't bet on how much their current balance is
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print("You do not have enought to bet that amount! Your current balance is: {balance}")
        else:
            break

    print(f'You are betting {bet} on {lines} lines. Total bet is equal to: {total_bet}')

    # slots is initally columns
    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
    print_slot_machine(slots)

main()