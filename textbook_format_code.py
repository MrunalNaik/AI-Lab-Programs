#dfs
graph = {}

n = int(input("Enter number of nodes: "))
for i in range(n):
    node = input("\nEnter node:     ")
    neighbours = input(f"Enter neighbours of {node}: ").split()
    graph[node] = neighbours
    
start = input("\nEnter start node: ")
goal = input("Enter goal node: ")


def ReconstructPath(nodePair, closed):
    path = [nodePair[0]]
    parent = nodePair[1]
    
    while parent is not None:
        path.insert(0, parent)
        
        for pair in closed:
            if pair[0] == parent:
                nodePair = pair
                
        parent = nodePair[1]
        
    return path


def OccursIn(node, nodeList):
    for pair in nodeList:
        if pair[0] == node:
            return True
    return False


def RemoveSeen(nodeList, open, closed):
    newList = []
    for node in nodeList:
        if not OccursIn(node, open) and not OccursIn(node, closed):
            newList.append(node)
    return newList


def MakePairs(nodeList, parent):
    pairList = []
    for node in nodeList:
        pairList.append((node, parent))
    return pairList


def DFS():
    open = [(start, None)]
    closed = []
    
    while open:
        print("\nOPEN:        ", open)
        print("CLOSED:      ", closed)
        
        nodePair = open.pop(0)
        node = nodePair[0]
        
        if node == goal:
            print("\nGoal Found")
            print("Final solution path: ", end="")
            for node in ReconstructPath(nodePair, closed):
                print(node, end=" ")
            return
        
        closed.insert(0, nodePair)
        
        children = graph[node]
        noLoops = RemoveSeen(children, open, closed)
        newList = MakePairs(noLoops, node)
        
        open = newList + open
        
    return "\nNo Solution Found"


DFS()



# #bfs
# graph = {}

# n = int(input("Enter number of nodes: "))
# for i in range(n):
#     node = input("\nEnter node: ")
#     neighbours = input(f"Enter neighbours of {node}: ").split()
#     graph[node] = neighbours
    
# start = input("\nEnter start node: ")
# goal = input("Enter goal node: ")


# def ReconstructPath(nodePair, closed):
#     path = [nodePair[0]]
#     parent = nodePair[1]
    
#     while parent is not None:
#         path.insert(0, parent)
        
#         for pair in closed:
#             if pair[0] == parent:
#                 nodePair = pair
#                 break
                
#         parent = nodePair[1]
        
#     return path


# def OccursIn(node, nodeList):
#     for pair in nodeList:
#         if pair[0] == node:
#             return True
#     return False


# def RemoveSeen(nodeList, open, closed):
#     newList = []
#     for node in nodeList:
#         if not OccursIn(node, open) and not OccursIn(node, closed):
#             newList.append(node)
#     return newList


# def MakePairs(nodeList, parent):
#     pairList = []
#     for node in nodeList:
#         pairList.append((node, parent))
#     return pairList


# def BFS():
#     open = [(start, None)]
#     closed = []
    
#     while open:
#         print("\nOPEN:        ", open)
#         print("CLOSED:      ", closed)
        
#         nodePair = open.pop(0)
#         node = nodePair[0]
        
#         if node == goal:
#             print("\nGoal Found")
#             print("Final solution path: ", end="")
#             for node in ReconstructPath(nodePair, closed):
#                 print(node, end=" ")
#             return
        
#         closed.insert(0, nodePair)
        
#         children = graph[node]
#         noLoops = RemoveSeen(children, open, closed)
#         newList = MakePairs(noLoops, node)
        
#         open = open + newList
        
#     return "\nNo Solution Found"


# BFS()



# #best first search
# graph = {}
# h = {}

# n = int(input("Enter number of nodes: "))
# for i in range(n):
#     node = input("\nEnter node: ")
#     value = int(input(f"Enter heuristics of {node}: "))
#     h[node] = value
#     neighbours = input(f"Enter neighbours of {node}: ").split()
#     graph[node] = neighbours
    
# start = input("\nEnter start node:  ")
# goal = input("Enter goal node:  ")
# isAscending = h[start] < h[goal]

# def ReconstructPath(nodePair, closed):
#     path = [nodePair[0]]
#     parent = nodePair[1]
    
#     while parent is not None:
#         path.insert(0, parent)
        
#         for pair in closed:
#             if pair[0] == parent:
#                 nodePair = pair
#                 break
            
#         parent = nodePair[1]
        
#     return path


# def OccursIn(node, nodeList):
#     for pair in nodeList:
#         if pair[0] == node:
#             return True
#     return False


# def RemoveSeen(nodeList, open, closed):
#     newList = []
#     for node in nodeList:
#         if not OccursIn(node, open) and not OccursIn(node, closed):
#             newList.append(node)
#     return newList


# def MakePairs(nodeList, parent):
#     pairList = []
#     for node in nodeList:
#         pairList.append((node, parent, h[node]))
#     return pairList


# def BestFirstSearch():
#     open = [(start, None, h[start])]
#     closed = []
    
#     while open:
#         print("\nOPEN:    ", open)
#         print("CLOSED:  ", closed)
        
#         nodePair = open.pop(0)
#         node = nodePair[0]
        
#         if node == goal:
#             print("\nGoal Found")
#             print("Final solution path: ", end="")
#             for node in ReconstructPath(nodePair, closed):
#                 print(node, end=" ")
#             return
        
#         closed.insert(0, nodePair)
        
#         children = graph[node]
#         noLoops = RemoveSeen(children, open, closed)
#         newList = MakePairs(noLoops, node)
        
#         open = newList + open
#         open.sort(key=lambda x: x[2], reverse=isAscending)
        
#     return "\nNo Solution Found"


# BestFirstSearch()