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


from random import randint, sample


X_SIZE = Y_SIZE = 5
CELLS = [(x, y) for y in range(Y_SIZE) for x in range(X_SIZE)]


def init_locations():
    """Pick random locations for player, exit door, and monster"""
    player, door, monster = sample(CELLS, k=3)

    return player, door, monster


def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    # if y == 0, can't move up
    # if y == max, can't move down
    # if x == 0, can't move left
    # if x == max, can't move right
    return moves


def move_player(player, move):
    # get the player's location
    # LEFT, x-1
    # RIGHT, x+1
    # UP, y-1
    # DOWN, y+1

    return player


def clip(val, val_min, val_max):
    """Constrain value between minimum and maximum"""
    return min(val_max, max(val_min, val))


def move_monster(monster):
    """Move monster to a random adjacent cell"""
    monster = (clip(monster[0] + randint(-1, 1), 0, X_SIZE-1),
               clip(monster[1] + randint(-1, 1), 0, Y_SIZE-1))
    return monster


if __name__ == '__main__':
    player, door, monster = init_locations()

    while True:
        print("Welcome to the dungeon!")
        print(f"You're currently in room {player}")
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
