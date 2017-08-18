''' guesser.py by Devin Carter, 08-18-2017
This program will ask the user to guess a random number between 1 and 100
'''

import random

# define main function
def main():
    print("Guess a number between 1 and 100")
    # randomNumber = 35 # for debugging only
    randomNumber = random.randint(1, 100)

    found = False  # flag variable to see if a correct guess has been made.

    # Run through the guessing program
    while not found:
        userGuess = int(input("Your Guess: ")) # turn str that is user guess into integer
        if userGuess == randomNumber:
            print("You got it right!")
            found = True
        elif userGuess > randomNumber:
            print("Guess a lower number!")
        else:
            print("Guess a higher number!")

    # Statement when game is won
    print("Thanks for playing!")





main()

