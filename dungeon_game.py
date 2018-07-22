#!/usr/bin/env python3


# draw grid
# pick random location for player
# pick random location for exit door
# pick random location for the monster
# draw player in the grid
# take input for movement
# move player, unless invalid move (past edges of grid)
# check for win/loss
# clear screen and redraw grid


X_SIZE = Y_SIZE = 5
CELLS = [(x, y) for y in range(Y_SIZE) for x in range(X_SIZE)]


def init_locations():
    """Pick random locations for player, exit door, and monster"""
    player = door = monster = None

    return player, door, monster


def move_player(player, move):
    # get the player's location
    # LEFT, x-1
    # RIGHT, x+1
    # UP, y-1
    # DOWN, y+1
    return player


if __name__ == '__main__':
    while True:
        print("Welcome to the dungeon!")
        print("You're currently in room {}") # fill with player position
        print("You can move {}") # fill with available moves
        print("Enter QUIT to quit")

        move = input("> ").upper()

        if move == "QUIT":
            break

        # Good move? Change player position
        # Bad move? Don't change anything
        # On the door? They win
        # On the monster? The lose
        # Otherwise, loop back around'
