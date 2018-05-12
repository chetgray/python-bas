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

import random

secret = random.randint(1, 10)

print("Guess a number from 1 to 10:")
while True:
    guess = int(input('>>> '))
    if guess < secret:
        print("Too low. Guess again:")
    elif guess > secret:
        print("Too high. Guess again:")
    else:
        print("Correct!")
        break
