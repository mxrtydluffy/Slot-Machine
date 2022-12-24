# Global constant
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

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

main()