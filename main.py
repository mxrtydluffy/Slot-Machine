import random

# Global constant
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

#Symbols
"""
What each reel has
A - represents most valueable
then going to the lowest.
"""

symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# Determining how much the value of each symbol
symbols_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    
    """
    Need to look at the rows the user bets on.
    - line will equal to 0
    - Column is set to 0 because the columns is set but not the rows.
    ____________________________________________________________________
    
    - First (for line in range(lines) we loop through every row and check what the user bets on.
    - Then the symbol we are checking (symbol = columns[0][line]) is whatever symbol is on the first column of the
    current row sice the symbols need to be the same.
    - "for column in columns" | Since we know the symbol we're going to check, we need to
    loop through every single column and check or that symbol
        - For each column "symbol_to_check" is assigned to the column at the current row that we are
        looking at. Ex.) row 0 looking you are at row 0, row 1, looking at row 1.
        - We then check is the symbols are the not same (if symbol !=) "symbol_to_check" if they are not
        the same we break out which means it checks the next line "for line in range(lines)" since user didn't
        win. If they are the same it doesn't break and once the for loop is completed we didn't break out since 
        the symbols are the same. The else statement is executed since the user won which is the miltipler values[symbol]
        times the bet on each line not total bet. Can win on one line but lose on the other.
    """

    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line +1)
    
    return winnings, winnings_lines # <- Total amount user won & what lines user won

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
    - "end" tells print statement what to end the line with since it's orignially \n
    """

    for row in range(len(columns[0])):
        # Print value that is at the first row of that column
        # loop through every single row
        for i, column in enumerate(columns):
            # For every row we loop through every column
            if i != len(columns) - 1:
                print(column[row], end =" | ")
            else:
                print(column[row], end="")
            
        # Every row needs to go down to the next line.
        print()

def deposit():

    """
    isdigit() tells if its a valid whole number. Since its a string we need
    a numeric value for deposit balance. The amount has to be greater than 0.
    If so the function stops but it its less than 0 it returns a print statement.
    The second else returns a print statement stating it must be a number.
    """

    while True:
        amount = input("How much would you like to deposit? \n$")
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
        lines = input("Enter the number on lines to bet on (1-" + str(MAX_LINES) + ")! \n")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.\n")
        else:
            print("Please enter a number.\n")

    return lines

def get_bet():
    while True:
        amount = input("How much would you like to bet? \n$")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.\n")

    return amount

def spin(balance):
    
    """
    Executes one game
    """

    lines = get_number_of_lines()

    # Can't bet on how much their current balance is
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount! Your current balance is: ${balance}\n")
        else:
            break

    print(f'You are betting {bet} on {lines} lines. Total bet is equal to: ${total_bet}\n')

    # slots is initally columns
    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbols_value)
    print(f'You won ${winnings}!!!')
    print(f'You won on lines:', *winning_lines)   # "*" is a splat operator is is going to pass every single line from the winning line list to the print function
    return winnings - total_bet    # <- Tells how much user won or lost from this spin.


def main():
    balance = deposit()
    while True:
        print(f"Current balance is: ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You are left with ${balance}\n")

main()