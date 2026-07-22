start = []
goal = []

print("\nEnter start state: ")
for i in range(3):
    start.extend(input().split())
    
print("\nEnter goal state: ")
for i in range(3):
    goal.extend(input().split())
    

def heuristic(node):
    h = 0
    for i in range(9):
        if node[i] != goal[i]:
            h += 1
    return h


def MoveGen(node):
    children = []
    idx = node.index('-')
    
    moves = {'U': idx - 3, 'D': idx + 3, 'L': idx - 1, 'R': idx + 1}
    
    for move, new_idx in moves.items():
        if move == 'U' and idx < 3:
            continue
        if move == 'D' and idx > 5:
            continue
        if move == 'L' and idx % 3 == 0:
            continue
        if move == 'R' and idx % 3 == 2:
            continue
        
        new_node = node.copy()
        new_node[idx], new_node[new_idx] = new_node[new_idx], new_node[idx]
        children.append(new_node)
        
    return children


def EightPuzzle():
    node = start
    step = 0
    
    while True:
        step += 1
        print(f"\nStep {step}:")
        for i in range(9):
            print(node[i], end=" ")
            if (i + 1) % 3 == 0:
                print()
        print("Heuristic value =", heuristic(node))
        
        if node == goal:
            print("\nGoal found")
            return  

        children = MoveGen(node)
        
        if not children:
            print("\nNo solution found")
            return
        
        children.sort(key=lambda x: heuristic(x))
        
        new_node = None
        plateau = False
        
        for child in children:
            if heuristic(child) < heuristic(node):
                new_node = child
                break
            if heuristic(child) == heuristic(node):
                plateau = True
                
        if new_node:
            node = new_node
        elif plateau:
            print("\nPlateau reached")
            return
        else:
            print("\nLocal optimum reached")
            return
        

EightPuzzle()