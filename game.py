"""A number-guessing game."""

from random import *

def guessing_game():
    '''
    Function selects a random int between 1 and 100, inclusive and engages
    user in a guessing game.
    '''
    name = input("Howdy, what's your name? \n (type in your name) ")
    number = randint(1, 100)
    print("%s, I'm thinking of a number between 1 and 100." % name)
    print("Try to guess my number.")
    # Looping through incorrect guesses
    tries = 0
    guess = 0
    while number != guess:       
        while True:
            raw_guess = input("Your guess? ")
            try:
                guess = int(raw_guess)
                break
            except ValueError:
                print("Sorry, please guess an integer.")
                #break
        print (guess)
        if guess < 101 and guess > 0:
            if number > guess:
                print("Your guess is too low, try again.")
                tries += 1
            elif number < guess:
                print("Your guess is too high, try again.")
                tries += 1
        else:
            print("Sorry, please guess an integer between 1 and 100.")
    print("Well done, %s! You found my number in %i tries!" % (name, tries))

guessing_game()
