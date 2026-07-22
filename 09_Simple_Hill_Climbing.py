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

    moved = False

    # First better neighbour
    for child in graph[current]:

        if heuristic[child] < heuristic[current]:

            parent = current
            current = child
            visited.append(current)
            moved = True
            break

        elif heuristic[child] == heuristic[current]:

            print("\nPlateau reached at", (current, parent, heuristic[current]))
            moved = False
            break

    if not moved:

        if current != goal:
            better = False

            for child in graph[current]:
                if heuristic[child] < heuristic[current]:
                    better = True

            if not better:

                if len(graph[current]) != 0 and heuristic[graph[current][0]] == heuristic[current]:
                    pass
                else:
                    print("\nLocal Minimum reached at", (current, parent, heuristic[current]))

        break

print("\nSequence of visited nodes:")
print(" -> ".join(visited))