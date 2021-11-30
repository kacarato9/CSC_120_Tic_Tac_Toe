def p_board():
    print(board[0])
    print(board[1])
    print(board[2])


def full():
    for i in board:
        for x in i:
            if x == '-':
                return False
    print("Tied game!")
    quit()


def check_win1():
    for i in range(length):
        win = True
        for x in range(length):
            if board[i][x] != "X":
                win = False
                break
        if win:
            print("player1 wins!")
            quit()
    for i in range(length):
        win = True
        for x in range(length):
            if board[x][i] != "X":
                win = False
                break
        if win:
            print("player1 wins!")
            quit()

    win = True
    for i in range(length):
        if board[i][i] != "X":
            win = False
            break
    if win:
        print("player1 wins!")
        quit()
    win = True
    for i in range(length):
        if board[i][length - 1 - i] != "X":
            win = False
            break
    if win:
        print("player1 wins!")
        quit()


def check_win2():
    for i in range(length):
        win = True
        for x in range(length):
            if board[i][x] != "O":
                win = False
                break
        if win:
            print("player2 wins!")
            quit()
    for i in range(length):
        win = True
        for x in range(length):
            if board[x][i] != "O":
                win = False
                break
        if win:
            print("player2 wins!")
            quit()
    win = True
    for i in range(length):
        if board[i][i] != "O":
            win = False
            break
    if win:
        print("player2 wins!")
        quit()
    win = True
    for i in range(length):
        if board[i][length - 1 - i] != "O":
            win = False
            break
    if win:
        print("player2 wins!")
        quit()


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
    check_win1()
    full()


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
    check_win2()
    full()


board = ['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']
p_board()
length = len(board)
while full() == False:
    player1(board)
    player2(board)


