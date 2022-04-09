#!/usr/bin/env python
#coding:utf-8

"""
Each sudoku board is represented as a dictionary with string keys and
int values.
e.g. my_board['A1'] = 8
"""
import os,sys
from BackTracking import BacktrackingSearch
from CSP import CSP
from AC3 import AC3
import time

ROW = "ABCDEFGHI"
COL = "123456789"


def print_board(board):
    """Helper function to print board in a square."""
    print("-----------------")
    for i in ROW:
        row = ''
        for j in COL:
            row += (str(board[i + j]) + " ")
        print(row)


def board_to_string(board):
    """Helper function to convert board dictionary to string for writing."""
    ordered_vals = []
    for r in ROW:
        for c in COL:
            ordered_vals.append(str(board[r + c]))
    return ''.join(ordered_vals)


def backtracking(board):
    """Takes a board and returns solved board."""
    board = CSP(board)
    AC3(board)
    solved_board = BacktrackingSearch(board)
    return solved_board


if __name__ == '__main__':

    usage = None
    file = sys.argv[0]
    input_string = sys.argv[1]
    line = str(input_string)

    
    # Setup output file
    out_filename = 'output.txt'
    outfile = open(out_filename, "w") 

    ROW = "ABCDEFGHI"
    COL = "123456789"

    # Parse boards to dict representation, scanning board L to R, Up to Down
    board = { ROW[r] + COL[c]: int(line[9*r+c]) for r in range(9) for c in range(9)}

    # Print starting board. TODO: Comment this out when timing runs.
    print_board(board)

    # start = time.process_time()
    # Solve with backtracking
    solved_board = backtracking(board)
    # end = time.process_time()
    # Print solved board. TODO: Comment this out when timing runs.
    print_board(solved_board)

    # Write board to file
    
    outfile.write(board_to_string(solved_board))
    outfile.write('\n')
    
