#Best First Search using a Priority Queue.

import heapq #Python's heapq implements a min-heap (priority queue).

def best_first_search(start):
    pq =[] # Initialize a priority queue (min-heap) to keep track of nodes to visit

    heapq.heappush(pq, (heuristic[start], start))  # Add the starting node to the priority queue with its heuristic value
    visited = set()  # Set to keep track of visited nodes

    while pq: # While there are nodes to visit
        h, node = heapq.heappop(pq) # Remove and return the node with the lowest heuristic value from the priority queue
        traversal.append(node) # Add the current node to the traversal path

        if node == goal: # If the current node is the goal, print the traversal path
            print("Traversal Order:",traversal)
            print("Solution Path:", path[node])
            return

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour) # mark the neighbour as visited
                heapq.heappush(pq, (heuristic[neighbour] , neighbour)) # Add the neighbour to the priority queue with its heuristic value

                path[neighbour] = path[node] + [neighbour]  # Update the path to the neighbour


    print("Traversal Order:", traversal)
    print("No path exists")

graph = {} #empty dictionary to store the graph
heuristic = {} #empty dictionary to store the heuristic values

n = int(input("Enter number of nodes:"))

for i in range(n):
    node = input("\nEnter node name:").upper()

    neighbours = input(f"Enter neighbours of {node} (separated by space): ").upper().split()  #neighbours = ['B', 'C'],because .split() converts the string into a list

    h = int(input(f"Enter heuristic value of {node} :"))

    graph[node]= neighbours;
    heuristic[node]= h

start = input("\nEnter starting node:").upper()
goal = input("Enter goal node:").upper()

visited = set()
traversal = []

path = {
    start: [start]  # Initialize the path dictionary with the starting node
}

best_first_search(start)