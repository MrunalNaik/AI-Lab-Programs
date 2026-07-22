board = [['-' for _ in range(3)] for _ in range(3)]

def print_board():
    for row in board:
        print(" ".join(row))
    print()

def is_moves_left():
    for row in board:
        if '-' in row:
            return True
    return False

def evaluate():
    # Rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '-':
            if board[i][0] == 'O':
                return 10
            else:
                return -10

    # Columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != '-':
            if board[0][j] == 'O':
                return 10
            else:
                return -10

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != '-':
        return 10 if board[0][0] == 'O' else -10

    if board[0][2] == board[1][1] == board[2][0] != '-':
        return 10 if board[0][2] == 'O' else -10

    return 0

def minimax(depth, isMax):

    score = evaluate()

    if score == 10:
        return score - depth

    if score == -10:
        return score + depth

    if not is_moves_left():
        return 0

    if isMax:

        best = -1000

        for i in range(3):
            for j in range(3):

                if board[i][j] == '-':

                    board[i][j] = 'O'

                    best = max(best, minimax(depth + 1, False))

                    board[i][j] = '-'

        return best

    else:

        best = 1000

        for i in range(3):
            for j in range(3):

                if board[i][j] == '-':

                    board[i][j] = 'X'

                    best = min(best, minimax(depth + 1, True))

                    board[i][j] = '-'

        return best


def find_best_move():

    bestVal = -1000
    bestMove = (-1, -1)

    for i in range(3):
        for j in range(3):

            if board[i][j] == '-':

                board[i][j] = 'O'

                moveVal = minimax(0, False)

                board[i][j] = '-'

                if moveVal > bestVal:

                    bestMove = (i, j)
                    bestVal = moveVal

    return bestMove


print_board()

while True:

    print("Your turn")

    r, c = map(int, input("Enter row and column (0-2): ").split())

    if board[r][c] != '-':
        print("Invalid move!\n")
        continue

    board[r][c] = 'X'

    print_board()

    if evaluate() == -10:
        print("You win!")
        break

    if not is_moves_left():
        print("It's a draw!")
        break

    print("Computer's turn")

    row, col = find_best_move()

    board[row][col] = 'O'

    print_board()

    if evaluate() == 10:
        print("Computer wins!")
        break

    if not is_moves_left():
        print("It's a draw!")
        break