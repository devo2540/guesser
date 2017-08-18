''' guesser.py by Devin Carter, 08-18-2017
This program will ask the user to guess a random number between 1 and 100
'''

import random

# define main function
def main():
    print("Guess a number between 1 and 100")
    randomNumber = 35
    # set randomNumber value to string
    randomNumber = str(randomNumber)

    found = False  # flag variable to see if a correct guess has been made.

    while not found:
        userGuess = input("Your Guess: ")
        if userGuess == randomNumber:
            print("You got it right!")
            found = True
        else:
            print("Sorry, try again.")


main()

