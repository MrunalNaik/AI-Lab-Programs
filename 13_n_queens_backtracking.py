n = int(input("Enter n: "))
x = [['-' for _ in range(n)] for _ in range(n)]


def Place(i, k):
    for j in range(k):
        if x[i][j] == 'Q':
            return False
    
    r, c = i, k
    while r >= 0 and c >= 0:
        if x[r][c] == 'Q':
            return False
        r -= 1
        c -= 1
        
    r, c = i, k
    while r < n and c >= 0:
        if x[r][c] == 'Q':
            return False
        r += 1
        c -= 1
    
    return True


def NQueens(k):
    for i in range(n):
        if Place(i, k):
            x[i][k] = 'Q'
            
            if k == n - 1:
                print("\nSolution")
                for row in x:
                    print(" ".join(row))
                print()
            else:
                NQueens(k + 1)
            
            x[i][k] = '-'
            

NQueens(0)