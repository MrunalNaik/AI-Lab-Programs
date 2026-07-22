graph = {}
heuristic = {}

n = int(input("Enter the number of nodes: "))

for i in range(n):

    node = input("\nNode: ")

    heuristic[node] = int(input("h(Node): "))

    graph[node] = {}

    neighbors = input("Neighbors (space separated): ").split()

    for neighbor in neighbors:
        cost = int(input(f"cost({node}->{neighbor}): "))
        graph[node][neighbor] = cost


start = input("\nEnter start node: ")
goal = input("Enter goal node: ")

open_list = [(start, None, 0, heuristic[start], heuristic[start])]
closed_list = []

iteration = 1

while open_list:

    open_list.sort(key=lambda x: x[4])  #For every element x, return its 5th item

    print(f"\nIteration {iteration}:")
    print("OPEN :", open_list)
    print("CLOSED:", closed_list)

    current = open_list.pop(0)

    node, parent, g, h, f = current

    closed_list.append(current)

    if node == goal:

        print("\nGoal Found")

        path = [goal]
        p = parent

        while p is not None:

            path.append(p)

            for item in closed_list:
                if item[0] == p:
                    p = item[1]
                    break

        path.reverse()

        print("Path:", " -> ".join(path))
        break

    for neighbor in graph[node]:

        cost = graph[node][neighbor]

        new_g = g + cost
        new_h = heuristic[neighbor]
        new_f = new_g + new_h

        found = False

        for item in closed_list:
            if item[0] == neighbor:
                found = True

        if not found:
            open_list.append((neighbor, node, new_g, new_h, new_f))

    iteration += 1