#!/usr/bin/python3
"""

Pick a random word from a list and then let the user guess letters
until they either get all the letters in the word or they run out of
chances.

*   make a list of words
*   pick a random word
*   draw spaces
*   take guesses
*   draw guessed letters and strikes
*   print out win/lose
"""

import random

words = ['jazzy', 'joked', 'jives', 'joker', 'fazes', 'foxed', 'hazes', 'faxed', 'jokes', 'faxes', 'foxes', 'waxes', 'fazed', 'babes',
         'jazzed', 'joking', 'fazing', 'faxing', 'jinxed', 'faking', 'hazing',
         'buzzing', 'jinxing', 'waxwing', 'quaking', 'queuing', 'skyjack', 'jaywalk',
         'jazziest', 'kookiest', 'alkaline', 'alkalize', 'revivify',
         'bubbliest', 'overjoyed', 'skyjacker', 'jaywalker',
         'zigzagging', 'revivified', 'skyjacking', 'jaywalking', 'alkalizing',
         'apple', 'banana', 'orange','coconut', 'strawberry', 'lime', 'grapefruit', 'lemon', 'kumquat', 'blueberry', 'melon']

secret = random.choice(words)
