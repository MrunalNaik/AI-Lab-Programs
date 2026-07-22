import random

n = int(input("Enter n: "))
board = list(range(n))


def printBoard():
    for i in range(n):
        for j in range(n):
            if board[j] == i:
                print("Q", end=" ")
            else:
                print("-", end=" ")
        print()
    

def safe():
    for i in range(n):
        for j in range(i + 1, n):
            if abs(board[i] - board[j]) == abs(i - j):
                return False
    return True


def NQueens():
    steps = 0
    
    print("\nInitial board")
    printBoard()
    
    while not safe():
        r1 = random.randint(0, n - 1)
        r2 = random.randint(0, n - 1)
        board[r1], board[r2] = board[r2], board[r1]
        
        steps += 1
        print(f"\nStep {steps}")
        printBoard()
        
    print("\nSolution found")
    
    
NQueens()