#!/usr/bin/env python3

"""
To Do:
1. Design the game board - DONE
2. Giving the user the choice betwen "X" and "O" - DONE
3. Design the game to be two-players - DONE
4. Give the option to play again
5. Determine win, loss, and tie
6. Develop an AI... BONUS points!!!
"""

import random

def printBoard(board):
    print(f"{board['7']}|{board['8']}|{board['9']}")
    print('-+-+-')
    print(f"{board['4']}|{board['5']}|{board['6']}")
    print('-+-+-')
    print(f"{board['1']}|{board['2']}|{board['3']}")


gameBoard = {'7': ' ', '8': ' ', '9': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '1': ' ', '2': ' ', '3': ' '}

turn = 'X'
count = 0

for i in range(10):
    printBoard(gameBoard)
    move = input(f"It's your turn, {turn}. Move to which place?")
    print(move)

    try:
        if gameBoard[move] == ' ':
            gameBoard[move] = turn
            count += 1
        else:
            print("That spot is taken.")
            continue
    except KeyError:
        print("That is not a valid space.")
        continue

    if count >= 5:
        if gameBoard['7'] == gameBoard['8'] == gameBoard['9'] != ' ': #across top check
            print("\nGame Over\n")
            print(f"****** {turn} won! ******")
            break
        if gameBoard['4'] == gameBoard['5'] == gameBoard['6'] != ' ': #across middle check
            print("\nGame Over\n")
            print(f"****** {turn} won! ******")
            break
        if gameBoard['1'] == gameBoard['2'] == gameBoard['3'] != ' ': #across bottom check
            print("\nGame Over\n")
            print(f"****** {turn} won! ******")
            break
        if gameBoard['1'] == gameBoard['4'] == gameBoard['7'] != ' ': # left check
            print("\nGame Over\n")
            print(f"****** {turn} won! ******")
            break
        if gameBoard['2'] == gameBoard['5'] == gameBoard['8'] != ' ': # center check
            print("\nGame Over\n")
            print(f"****** {turn} won! ******")
            break
        if gameBoard['3'] == gameBoard['6'] == gameBoard['9'] != ' ': # right check
            print("\nGame Over\n")
            print(f"****** {turn} won! ******")
            break
        if gameBoard['1'] == gameBoard['5'] == gameBoard['9'] != ' ': # diagonal
            print("\nGame Over\n")
            print(f"****** {turn} won! ******")
            break
        if gameBoard['7'] == gameBoard['5'] == gameBoard['3'] != ' ': # diagonal
            print("\nGame Over\n")
            print(f"****** {turn} won! ******")
            break
        

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(gameBoard)  
