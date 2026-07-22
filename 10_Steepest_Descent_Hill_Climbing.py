graph = {}
heuristic = {}

n = int(input("Enter the number of nodes: "))

for i in range(n):
    node = input("\nNode: ")
    heuristic[node] = int(input("Heuristics: "))
    neighbors = input("Neighbors(separated by spaces) : ").split()
    graph[node] = neighbors

start = input("\nEnter start node: ")
goal = input("Enter goal node: ")

current = start
parent = None
visited = [current]

while True:

    print("\nNode")
    print((current, parent, heuristic[current]))

    children = []

    for child in graph[current]:
        children.append((child, current, heuristic[child]))

    print("Children")
    print(children)

    if current == goal:
        print("\nGoal Found")
        break

    if len(graph[current]) == 0:
        print("\nLocal Minimum reached at", (current, parent, heuristic[current]))
        break

    # Find best neighbour
    best = graph[current][0]

    for child in graph[current]:
        if heuristic[child] < heuristic[best]:
            best = child

    if heuristic[best] < heuristic[current]:

        parent = current
        current = best
        visited.append(current)

    elif heuristic[best] == heuristic[current]:

        print("\nPlateau reached at", (current, parent, heuristic[current]))
        break

    else:

        print("\nLocal Minimum reached at", (current, parent, heuristic[current]))
        break

print("\nSequence of visited nodes:")
print(" -> ".join(visited))