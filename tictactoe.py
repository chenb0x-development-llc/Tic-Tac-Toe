#!/usr/bin/env python3

"""
To Do:
4. Give the option to play again - DONE
6. Develop an AI... BONUS points!!!
"""

import random

def printBoard(board):
    print(f"{board['7']}|{board['8']}|{board['9']}")
    print('-+-+-')
    print(f"{board['4']}|{board['5']}|{board['6']}")
    print('-+-+-')
    print(f"{board['1']}|{board['2']}|{board['3']}")


play = 'y'

while play == "y":
    count = 0
    gameBoard = {'7': ' ', '8': ' ', '9': ' ',
                 '4': ' ', '5': ' ', '6': ' ',
                 '1': ' ', '2': ' ', '3': ' '}
    turn = 'X'
    while count <= 9:  # Change from a for loop to work with a count that changes on condition of proper space selection.
        printBoard(gameBoard)
        if turn == 'X': # This conditional allowed for play against computer, but removed PvP capability. Needs to be fixed
            move = input(f"It's your turn, {turn}. Move to which place?")
            print(move)
        else:
            move = str(random.randint(1,9))

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
    play = input("Would you like to play again? (Y)es/(N)o")
    play = play.lower()
  
