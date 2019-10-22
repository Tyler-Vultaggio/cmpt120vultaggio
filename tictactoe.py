# CMPT 120 Intro to Programming
# Lab #6 – Lists and Error Handling
# Author: Your Name Here
# Created: YYYY-MM-


symbol = [ " ", "x", "o" ]

def printRow(row):
    rowStr = "| "
    for cell in row:
        rowStr = rowStr + symbol[cell] + " | "
    print(rowStr)

def printBoard(board):
    print("+-----------+")
    for i in range(3):
        printRow(board[i])
        print("+-----------+")
    pass

def markBoard(board, row, col, player):
    # check to see whether the desired square is blank
    # if so, set it to the player number
    if board[row][col] == int(0):
        board[row][col] = player
        return True
    else:
        return False

def getPlayerMove():
    row = int(input("Enter your row: "))
    col = int(input("Enter your columon: ")) # prompt the user separately for the row and column numbers
    return (row,col) # then return that row and column instead of (0,0)

def hasBlanks(board):
    # for each row in the board...
    for row in board:
        for col in row:
            if col == 0:
                return True
    return False
    # for each square in the row...
    # check whether the square is blank
    # if so, return True

def main():
    board = [[0,0,0],
             [0,0,0],
             [0,0,0]] # TODO replace this with a three-by-three matrix of zeros
    player = 1
    while hasBlanks(board):
        printBoard(board)
        row,col = getPlayerMove()
        if not markBoard(board,row,col,player):
            print("That postion was taken.")
        else:
            player = player % 2 + 1 # switch player for next turn
    printBoard(board)
main()














