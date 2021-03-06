#!/usr/bin/python3
"""

*   generate a random number between 1 and 10
*   get a number guess from the player
*   compare guess to secret number
*   print hit/miss

Refinement:
*   Limit the number of guesses
*   Catch when someone submits a non-integer
*   Print "too low" or "too high" messages for bad guesses
*   Let people play again

https://teamtreehouse.com/library/number-game-introduction
"""

from random import randint
from math import sqrt

min_num = 1
max_num = 10

def game():
    secret = randint(min_num, max_num)

    print("Guess a number from 1 to 10:")
    for guess_num in range(int(sqrt(max_num - min_num)), 0, -1):
        while True:
            try:
                guess = int(input('({} guesses remain) >>> '.format(guess_num)))
            except ValueError:
                print("Please enter a number:")
                continue
            else:
                break

        if guess < secret:
            print("Too low. Guess again:")
        elif guess > secret:
            print("Too high. Guess again:")
        else:
            print("Correct!")
            break
    else:
        print("Sorry, you ran out of guesses. The number was {}.".format(secret))

playing = True
while playing:
    game()
    again = None
    while True:
        again = input("Would you like to play again? [y/N]: ").lower()
        if again in ('y', 'yes'):
            break
        elif again in ('n', 'no', ''):
            playing = False
            break
        else:
            print("Invalid selection.")
