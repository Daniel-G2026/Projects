# -------- Python Banking Program -----------
#
# Show balance
# Deposit
# Withdrawl
import sys
def main():

    print("-----Python Banking Program------")
    balance = 0
    show_balance(balance)
    make_deposit = input("Would you like to make a deposit? Enter (y = yes / n = no) : ")
    if make_deposit.lower() == "y":
        balance=deposit(balance)
        show_balance(balance)
    else:
        print("Thank you for coming!")
        print("Have a good day.")
        exit()
    functionality(balance)


def functionality(balance):
    while True:
        answer = input("What would you like to do? (Select the number corresponding to on of the following functionality):\n"
                       "1. Show balance\n"
                       "2. Make a deposit\n"
                       "3. Make a withdrawal\n"
                       "4. exit program\n")
        try:
           answer = int(answer)
        except ValueError:
            print("amount entered is invalid")
            continue
        else:
            if answer == 1:
                show_balance(balance)
            elif answer == 2:
                balance = deposit(balance)
            elif answer == 3:
                balance = withdraw(balance)
            else:
                print("Thank you for using our services. Hope to see you soon!")
                break


def deposit(balance):
    while True: # infinite loop until an acceptable amount has been inputted
        try:
            amount = float(input("How much would you like to deposit?  "))

        except ValueError: #check to see if amount entered is of the correct value type
            print(f"amount entered is invalid")
            continue # go back to start of program
        else: # if no value error continue program
              if amount < 0:
                  print("Money deposited cannot be negative")
                  continue
              # elif amount == 1:
              #     return balance
              else:
                balance+= amount
                return balance

def show_balance(balance):
    print(f"You currently have a total of ${balance:.2f} with us.")
    print()
    print()

def withdraw(balance):
    while True:  # infinite loop until an acceptable amount has been inputted
        if balance == 0:
            print("You currently have no money with us and therefore cannot withdraw.")
            return balance
        try:
            amount = float(input("How much would you like to withdraw? "))

        except ValueError:  # check to see if amount entered is of the correct value type
            print(f"amount entered is invalid")
            continue  # go back to start of program
        else:  # if no value error continue program
            if amount < 0:
                print("Money deposited cannot be negative")
                continue
            elif amount > balance:
                print(f"Insufficient funds.")
                continue
            #elif amount ==1:
            #   return balance
            else:
                balance -= amount
                return balance

if __name__ == '__main__':
    main()
