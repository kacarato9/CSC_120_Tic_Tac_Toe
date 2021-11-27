board = ['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']

def p_board():
    print(board[0])
    print(board[1])
    print(board[2])

def player1(board):
    print("Player 1, please make your move.")
    again = True
    while again == True:
        row = int(input("Enter row number (0-2): "))
        while row > 2 or row < 0:
            print("Invalid row, Please re-enter row 0-2")
            row = int(input("Enter row number (0-2): "))
        col = int(input("Enter col number (0-2): "))
        while col > 2 or col < 0:
            print("Invalid col, Please re-enter col 0-2")
            col = int(input("Enter col number (0-2): "))
        if board[row][col] == '-':
            board[row][col] = "X"
            again = False
        else:
            print("row:", row, "col:", col, " has already been taken, please select again.")
            again = True
    p_board()

def player2(board):
    print("Player 2, please make your move.")
    again = True
    while again == True:
        row = int(input("Enter row number (0-2): "))
        while row > 2 or row < 0:
            print("Invalid row, Please re-enter row 0-2")
            row = int(input("Enter row number (0-2): "))
        col = int(input("Enter col number (0-2): "))
        while col > 2 or col < 0:
            print("Invalid col, Please re-enter col 0-2")
            col = int(input("Enter col number (0-2): "))
        if board[row][col] == '-':
            board[row][col] = "O"
            again = False
        else:
            print("row:", row, "col:", col, " has already been taken, please select again.")
            again = True
    p_board()

p_board()
for i in board:
    for x in i:
        if x == '-':
            player1(board)
            player2(board)
