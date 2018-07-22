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
