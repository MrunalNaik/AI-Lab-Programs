from collections import deque

def bfs_waterjug(cap1, cap2, target):

    queue = deque([((0, 0), [((0, 0), "Initial State")])])
    visited = set()

    while queue:

        (x, y), path = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))

        if x == target or y == target:

            print("\nSolution found in", len(path)-1, "steps:\n")

            for i, (state, action) in enumerate(path):
                print(f"Step {i}:")
                print(f"Jug1 = {state[0]}L\t|\tJug2 = {state[1]}L\t<-- {action}")

            return

        next_states = [

            ((cap1, y), "Fill Jug 1"),

            ((x, cap2), "Fill Jug 2"),

            ((0, y), "Empty Jug 1"),

            ((x, 0), "Empty Jug 2"),

            ((max(0, x-(cap2-y)), min(cap2, y+x)),
             "Pour from Jug 1 into Jug 2"),

            ((min(cap1, x+y), max(0, y-(cap1-x))),
             "Pour from Jug 2 into Jug 1")

        ]

        for state, action in next_states:
            if state not in visited:
                queue.append((state, path + [(state, action)]))

    print("No Solution Found")


cap1 = int(input("Enter the capacity of Jug 1: "))
cap2 = int(input("Enter the capacity of Jug 2: "))
target = int(input("Enter the target amount: "))

bfs_waterjug(cap1, cap2, target)