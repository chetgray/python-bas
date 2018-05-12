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

print("Add items to your list,\nor enter 'DONE' to quit:")
while True:
    user_input = input(">>> ")
    if user_input == 'DONE':
        break
    shopping_list.append(user_input)

print("\nHere's everything that's on your list:")
for item in shopping_list:
    print(u" ☐ {}".format(item))
