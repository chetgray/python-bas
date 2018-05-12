#!/usr/bin/python3
"""

*   generate a random number between 1 and 10
*   get a number guess from the player
*   compare guess to secret number
*   print hit/miss

https://teamtreehouse.com/library/number-game-introduction
"""

import random

secret = random.randint(1, 10)

print("Guess a number from 1 to 10:")
while True:
    guess = int(input('>>> '))
    if guess == secret:
        print("Correct!")
        break
    else:
        print("Incorrect. Guess again:")
