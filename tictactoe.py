#!/usr/bin/env python3

"""
To Do:
1. Design the game board - DONE
2. Giving the user the choice betwen "X" and "O"
3. Design the game to be two-players
4. Give the option to play again
6. Develop an AI... BONUS points!!!
"""

import random

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


gameBoard = {'7': ' ', '8': ' ', '9': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '1': ' ', '2': ' ', '3': ' '}

printBoard(gameBoard)

"""
board_keys = []

for key in gameBoard:
    board_keys.append(key)
"""

