# PROFESSIONAL PORTFOLIO PROJECT
# PROJECT NAME - Tic Tac Toe
# PROJECT FUNCTIONALITY - A text-based Python program implementation of the Tic-Tac-Toe game.

import numpy as np

cells = [num + 1 for num in range(9)]


def display_game_board():
    """Displays the board of the tic-tac-toe game."""
    print()
    print("|-----|-----|-----|")
    print(f"|  {cells[0]}  |  {cells[1]}  |  {cells[2]}  |")
    print("|-----|-----|-----|")
    print(f"|  {cells[3]}  |  {cells[4]}  |  {cells[5]}  |")
    print("|-----|-----|-----|")
    print(f"|  {cells[6]}  |  {cells[7]}  |  {cells[8]}  |")
    print("|-----|-----|-----|")
    print()


def prompt_player_move(player_id):
    """Prompts a player to make their move, i.e. to fill a chosen cell with their icon."""
    player_icon = np.where(player_id == 1, "X", "O")
    valid_choice = False
    while not valid_choice:
        print(f"Player {player_id}, please make your move.")
        player_cell_choice = int(input(f"Enter the cell number you want to fill (from 1-9): ").strip())
        if player_cell_choice in range(1, 10):
            if cells[player_cell_choice - 1] in ["X", "O"]:
                print("Cell already been populated.")
                display_game_board()
                continue
            else:
                cells[player_cell_choice - 1] = player_icon
            valid_choice = True
            print()
        else:
            print("ERROR. That is an invalid input. Please choose a number between 1 and 9.")
            print()


def a_win(player_id):
    """Checks if any of the players has won the game and returns a boolean True if so."""
    player_icon = np.where(player_id == 1, "X", "O")
    if (cells[0] == cells[1] == cells[2] == player_icon or cells[3] == cells[4] == cells[5] == player_icon or \
        cells[6] == cells[7] == cells[8] == player_icon or cells[0] == cells[3] == cells[6] == player_icon or \
        cells[1] == cells[4] == cells[7] == player_icon or cells[2] == cells[5] == cells[8] == player_icon or \
        cells[0] == cells[4] == cells[8] == player_icon or cells[2] == cells[4] == cells[6] == player_icon):
        print(f"PLAYER {player_id} WINS.")
        return True
    else:
        return False


def a_draw():
    """Checks for a draw in the game and returns a boolean True if there is."""
    # Implemented with Numpy functions; others ways are possible.
    array = np.array(cells)                 # with numpy array(), create an array from "cells"
    unique_values = np.unique(array)        # with numpy unique(), get the unique values of "array" by removing duplicate values

    # check if the array has reduced to only 2 unique values (would be so if all 9 cells have been filled with either "X" or "O")
    if len(unique_values) == 2:
        print("THERE IS A DRAW.")
        return True


print("\n ********* WELCOME TO THE TIC-TAC-TOE GAME ***** \n")

display_game_board()

while True:
    prompt_player_move(player_id=1)
    display_game_board()
    if a_win(player_id=1):
        break
    elif a_draw():
        break
    prompt_player_move(player_id=2)
    display_game_board()
    if a_win(player_id=2):
        break
    elif a_draw():
        break
