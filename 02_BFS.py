# Breadth First Search (BFS)
# BFS uses Queue (FIFO).

from collections import deque #Python provides a queue called deque.

# queue = deque()  # Initialize a queue to keep track of nodes to visit

# queue.append("A") #adds from rear/back/right of the queue
# queue.popleft()  # Remove and return the leftmost/first item from the queue

def bfs(start):

    queue = deque([start])  # Initialize a queue with the starting node
    visited = set()  # Set to keep track of visited nodes

    while queue: # While there are nodes to visit
        node = queue.popleft() # Remove and return the leftmost/first item from the queue
        traversal.append(node) # Add the current node to the traversal path

        if node == goal: # If the current node is the goal, print the traversal path
            print("Traversal Order:", traversal)
            print("solution Path:", path[node])
            return 

        for neighbour in graph[node]: # Visit Neighbours
            if neighbour not in visited:
                visited.add(neighbour)  # Mark the neighbour as visited
                queue.append(neighbour)  # Add the neighbour to the queue


                path[neighbour] = path[node] + [neighbour]  # Update the path to the neighbour

    print("Traversal Order:", traversal)
    print("No path found from", start, "to", goal)


graph = {} #empty dictionary to store the graph

n = int (input("Enter number of nodes:"))

for i in range(n):
    node = input("\nEnter node name:").upper()

    neighbours = input(f"Enter neighbours of {node} (separated by space): ").upper().split()  #neighbours = ['B', 'C'],because .split() converts the string into a list.
    graph[node] =neighbours

start = input("\nEnter starting node:").upper()
goal = input("Enter goal node:").upper()

visited = set()
traversal = []  # List to keep track of the order of traversal

path ={
    start: [start]  # Initialize the path dictionary with the starting node
}

bfs(start)