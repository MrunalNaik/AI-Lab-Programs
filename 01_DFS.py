# Depth First Search (DFS)
#DFS Uses Stack (or recursion).

visited = set()  # Set to keep track of visited nodes

def dfs(node, path): 
    visited.add(node)  # Mark the current node as visited
    path.append(node)  # Add the current node to the path

    if node == goal: # If the current node is the goal, print the path
        print("\nSolution Path:", path)
        return True

    for neighbour in graph[node]: # Visit Neighbours
        if neighbour not in visited:  # If the neighbour has not been visited
            if dfs(neighbour, path):  # Recursively call dfs on the neighbour
                return True

    path.pop() # Backtrack: remove the current node from the path if goal not found
    return False  # Return False if the goal is not found in this path

graph = {} #empty dictionary to store the graph

n = int(input("Enter number of nodes:"))

for i in range(n):
    node = input("\nEnter node name: ").upper()

    neighbours = input(f"Enter neighbours of {node} (separated by space): ").upper().split()  #neighbours = ['B', 'C'],because .split() converts the string into a list.

    graph[node] = neighbours

start = input("\nEnter starting node: ").upper()
goal = input("Enter goal node: ").upper()

visited = set()

print("\nDFS Traversal :")

if not dfs(start,[]): #[] initailly empty list
    print("No path found from", start, "to", goal)



