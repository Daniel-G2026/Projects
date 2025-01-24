#Python Slot Machine
import Banking_Program as bank
import random

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
    results =[]
    for symbol in range(3):
        results.append(random.choice(symbols))  #randomly pick a symbol and add to results list
    return results


def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")
    # join is a function used to join iterables together. Here it is joining the iterable row with a "|" (space)

def get_payout(row,bet):
    count = 0
    unique_value = set(row)  # using the set() function i converted the list row to a set, remember sets cant have duplicates
    if len(unique_value) == 1:      #There is only 1 unique symbol in row ( indicating 3 same symbols so win)
        print(f"You won ${bet *3}!!!\n")
        return bet * 3

    elif len(unique_value) == 2: #T There are only 2 unique symbols in row (indicating 2 symbols are the same so close call)
        print("So close")
        return 0
    else:
        return 0

def main():

    print("***********************")
    print("Welcome to Python Slots")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐") #  windows plus ; gives you emoji
    print("************************")
    balance = bank.deposit(0)
    first_iteration = True

    while True:
        print(f"current balance: ${balance}")
        # if not first_iteration:
        #     play_again = input("Would you like to continue playing? (y/n): ").strip().lower()
        #     if play_again != 'y':
        #         bank.show_balance(balance)
        #         print("Thank you for playing!")
        #
        #         break


        if first_iteration == True:
            bet = input("Place your bet amount: ")
            if not bet.isdigit():
                print("Please enter a valid number")
                continue
            bet = int(bet)
        else:
            bet = input("Place your bet amount (enter x to quit): ")
            if bet.lower().strip() == "x":
                print("Thanks for playing")
                break
            elif not bet.isdigit():
                print("Please enter a valid number")
                continue
            bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            choice = input("Would you like to deposit more funds?: (y/n) ")
            if choice.lower() == 'y':
                balance = bank.deposit(balance)
                continue
            else:
                continue

        elif bet <= 0:
            print("Bet must be greater than 0")
            continue
        balance -= bet
        row = spin_row()
        print("Spinning....\n")
        print_row(row)
        payout = get_payout(row, bet)
        balance += payout
        if balance == 0:
            bank.show_balance(balance)
            choice2 = input("Would you like to deposit more funds?: (y/n) ")
            if choice2.lower().strip() == 'y':
                balance = bank.deposit(balance)
                continue
            else:
                print("Thank you for playing!")
                break
        play_again = input("Would you like to continue playing? (y/n): ").strip().lower()
        if play_again != 'y':
            bank.show_balance(balance) # can add question to prompt withdraw, or not and when i learn how to store memory
                                        # the next time they place
                                        # they will start with remaining balance
            print(f"Thank you for playing! Your balance is {balance}")
            break


if __name__ == '__main__':
    main()

