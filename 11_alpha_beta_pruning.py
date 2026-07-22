INF = float('inf')

graph = {}
leaves = {}

n = int(input("\nEnter number of nodes: "))

for i in range(n):
    print(f"\nNode {i}")
    children = input("Children: ").split()
    if not children:
        value = int(input("Value: "))
        leaves[str(i)] = value
    graph[str(i)] = children
    

def AlphaBeta(node, alpha, beta, isMax, depth):
    print(f"\nExploring node  : {node}")
    print(f"Level           : {depth}", "[LEAF]" if node in leaves else "[MAX]" if isMax else "[MIN]")
    if node in leaves:
        print(f"Value           : {leaves[node]}")
        return leaves[node]
    else:
        print(f"Alpha = {alpha}, Beta = {beta}")
        
    if isMax:
        for child in graph[node]:
            alpha = max(alpha, AlphaBeta(child, alpha, beta, not isMax, depth + 1))
            
            print(f"\nExploring node  : {node}")
            print(f"Level           : {depth}", "[MAX]")
            print(f"Alpha = {alpha}, Beta = {beta}")
            
            if alpha >= beta:
                print(f"Pruning remaining children of node {node}")
                break
        
        return alpha
    
    else:
        for child in graph[node]:
            beta = min(beta, AlphaBeta(child, alpha, beta, not isMax, depth + 1))
            
            print(f"\nExploring node  : {node}")
            print(f"Level           : {depth}", "[MIN]")
            print(f"Alpha = {alpha}, Beta = {beta}")
            
            if alpha >= beta:
                print(f"Pruning remaining children of node {node}")
                break
        
        return beta
    
    
print("\nOptimal value:", AlphaBeta("0", -INF, INF, True, 0))