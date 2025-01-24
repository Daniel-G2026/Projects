#Hangman in python
import random


words = ["apple","orange","banana","coconut","pineapple"]



#dictionary of key:()     (key to tuple)
hangman_art = { 0: ("   ",
                    "   ",
                    "   ",),
                1: (" o ",
                    "   ",
                    "   "),
                2: (" o ",
                    " | ",
                    "   "),
                3: (" o ",
                    "/| ",
                    "   "),
                4: (" o ",
                    "/|\\",
                    "   "),
                5: (" o ",
                    "/|\\",
                    "/  "),
                6: (" o ",
                    "/|\\",
                    "/ \\")}

def display_man(wrong_guesses):
    for string in hangman_art[wrong_guesses]:
        print(string)

def display_hint(hint):     #hint is going to be a list of underscores, for each letter we guess right, on of those underscores will change to that letter
    return "".join(hint)

def display_answer(answer):
    print(answer)

def main ():
    print("--------------------------------------")
    print("Welcome to the Hangman game in python!")
    print("--------------------------------------")
    answer = random.choice(words)
    hint = [ '_' for i in answer]
    wrong_guesses = 0
    letter_guessed = []
    while True:
        try:
            guess = input("Guess the letter: ")   #try to assign input unless value error
        except ValueError:
            print("Invalid letter. Try again")
            continue

        else:
            if guess in answer and guess not in hint:  #only try this if guess is in answer and not in hint to prevent repeated guesses of same letter
                for i,letter in enumerate(answer):    #using a for loop to iterate over the entire answer to also handle duplicate letters
                     if guess == letter and hint[i] == "_":
                            hint[i] = guess

                print(display_hint(hint))
                display_man(wrong_guesses)

            elif guess not in answer or guess in hint:   # handling already guessed correct guesses  and wrong guesses
                 if wrong_guesses < 6:
                     if guess not in letter_guessed:    #handling already guessed wrong guesses
                         print("You guessed wrong")
                         # if guess in letter_guessed:        #checking if guessed word is
                         #     print("You already guessed this letter")
                         #     continue
                         wrong_guesses +=1
                         display_man(wrong_guesses)
                         display_hint(hint)
                         letter_guessed.append(guess)    #Keep track of already guessed words
                     else:                                 #if guess is has already been guessed
                         print("You already guessed this word")
                         continue

                 elif wrong_guesses ==6:   #If wrong guess ==6 you lost the game
                        print("Hangman has been completed, you lost.")
                        print("-------------------------------------\n")

                        choice = input("Would you like to play again? (Y/N): ")
                        if choice.upper().strip() != 'Y':
                            print("Thanks for playing!")
                            break
                        else:
                            hint =  [ '_' for i in answer]
                            wrong_guesses = 0
                            answer = random.choice(words)

            if answer== "".join(hint): #Hint is a list and answer is a string, so needed to convert hint to a string
                 print("You won!")
                 break














if __name__ == '__main__':
    main()
