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


def OccursIn(node, nodeList):
    for _node in nodeList:
        if _node == node:
            return True
    return False


def RemoveSeen(nodeList, open, closed):
    newList = []
    for node in nodeList:
        if not OccursIn(node, open) and not OccursIn(node, closed):
            newList.append(node)
    return newList


def EightPuzzle():
    open = [start]
    closed = []
    step = 0
    
    while open:
        open.sort(key=lambda x: heuristic(x))
        node = open.pop(0)
        
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
        
        closed.insert(0, node)
        
        children = MoveGen(node)
        noLoops = RemoveSeen(children, open, closed)
        
        open = open + noLoops
    
    return "No solution found"


EightPuzzle()






# output:
# Enter start state: 
# 1 2 3
# 4 5 6
# 7 - 8

# Enter goal state: 
# 1 2 3
# 4 5 6
# 7 8 -