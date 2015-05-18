#!/usr/bin/python

# Head ends here
def next_move(posr, posc, board):
    if(posr % 2 == 0):
        if(board[posr][posc] == 'd'):
            print("CLEAN")
        elif((posc == 4) and (posr < 4)):
            print("DOWN")
        else:
            print("RIGHT")
    else:
        if(board[posr][posc] == 'd'):
            print("CLEAN")
        elif((posc == 0) and (posr < 4)):
            print("DOWN")
        else:
            print("LEFT")

# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)

