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


def draw_grid(player, door, monster):
    grid = [['.'] * X_SIZE for y in range(Y_SIZE)]
    grid[player[1]][player[0]] = '@'
    grid[door[1]][door[0]] = '<'
    grid[monster[1]][monster[0]] = 'M'

    print('\n'.join(''.join(r) for r in grid))


def get_moves(player):
    moves = {"LEFT", "RIGHT", "UP", "DOWN"}
    # if x == 0, can't move left
    # if x == max, can't move right
    # if y == 0, can't move up
    # if y == max, can't move down
    if player[0] == 0:
        moves.discard("LEFT")
    elif player[0] == X_SIZE-1:
        moves.discard("RIGHT")
    if player[1] == 0:
        moves.discard("UP")
    elif player[1] == Y_SIZE-1:
        moves.discard("DOWN")

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
        draw_grid(player, door, monster)
        print("Welcome to the dungeon!")
        print(f"You're currently in room {player}")
        print(f"You can move {', '.join(get_moves(player))}")
        print("Enter QUIT to quit")

        move = input("> ").upper()

        if move == "QUIT":
            break

        # Good move? Change player position
        # Bad move? Don't change anything
        # On the door? They win
        # On the monster? The lose
        # Otherwise, loop back around'
