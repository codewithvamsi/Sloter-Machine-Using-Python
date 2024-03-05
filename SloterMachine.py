import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "$":2,
    "&":4,
    "!":6,
    "#":8,
}

symbol_values = {
    "$":5,
    "&":4,
    "!":3,
    "#":2,
}
def check_winnigs(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            all_symbol_chech = column[line]
            if symbol != all_symbol_chech:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings,winning_lines

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range (cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range (rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(column) -1: #maxindex
                print(column[row], end= " | ")
            else:
                print(column[row],  end= "")
        print()


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                # print(amount)
                break
            else:
                print("Amount must be Greater then 0.")
        else:
         print("Enter a valid number.")
    return amount

def get_number_lines():
    while True:
        lines = input(f"Enter the amount of lines to bet on 1 - {MAX_LINES} ? ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <=3:
                # print(lines)
                break
            else:
                print("Lines must be Greater then 0 and " + str(MAX_LINES) )
        else:
            print("Enter a valid number.")
    return lines

def get_bet():
    while True:
        bet = input(f"Enter the amount  of bet between ${MIN_BET} - ${MAX_BET} ? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET<= bet <=MAX_BET:
                # print(lines)
                break
            else:
                print(f"Enter valid bet between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Enter a valid number.")
    return bet

def spin(balance):
    lines = get_number_lines()
    while True:
        bet = get_bet()
        total_Bet = bet * lines

        if total_Bet > balance:
            print(f"Your balance is not enought to bet. Your Balance is ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines and total bet is ${total_Bet}")

    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings,winning_lines = check_winnigs(slots,lines,bet,symbol_values)
    print(f"you won ${winnings}")
    print(f"you won on lines: ", *winning_lines)
    return winnings - total_Bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        ans = input("Press enter to play and (q to quit).")
        if ans.lower() == 'q':
            break
        balance += spin(balance)
    print(f"your are left with ${balance}")

main()
