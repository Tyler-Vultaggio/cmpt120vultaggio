# CMPT 120 Intro to Programming
# Lab #6 – Lists and Error Handling
# Author: Tyler Vultaggio
# Created: 10-22-2019


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

def markBoard(board, row, col, player):
    if board[row][col] == int(0):
        board[row][col] = player
        return True
    else:
        return False

def getPlayerMove():
    row = int(input("Enter your row: "))
    col = int(input("Enter your columon: "))
    return (row,col)

def hasBlanks(board):
    for row in board:
        for col in row:
            if col == 0:
                return True
    return False

def main():
    board = [[0,0,0],
             [0,0,0],
             [0,0,0]]
    player = 1
    while hasBlanks(board):
        printBoard(board)
        row,col = getPlayerMove()
        if not markBoard(board,row,col,player):
            print("That postion was taken.")
        else:
            player = player % 2 + 1
    printBoard(board)
main()














