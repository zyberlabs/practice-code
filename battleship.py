#!/usr/bin/python

=begin

   Battleship!
   Author: Me!
   Date: 01/15/15
   From: Codecademy

=end

from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "\r\nLet's play Battleship!\r\n"
#print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
#print ship_row
#print ship_col

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(4):
    print "Turn", (turn + 1)
    print_board(board)
    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!\r\n"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or \
           (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean.\r\n"
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already.\r\n"
        else:
            print "You missed my battleship!\r\n"
            board[guess_row][guess_col] = "X"
            if turn == 3:
                print "Game Over\r\n"
