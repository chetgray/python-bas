#!/usr/bin/python3
"""Shopping List To-Do List

*   Run the script to start using it
*   Put new things in the list, one at a time
*   Enter the word DONE - in all caps - to quit the program
*   And, once I quit, I want the app to show me everything that's
    on my list

https://teamtreehouse.com/library/shopping-list-introduction
"""

shopping_list = []

user_input = ""
while user_input != 'DONE':
    user_input = input("Enter an item to add to the list, or 'DONE' to quit: ")
    shopping_list.append(user_input)
