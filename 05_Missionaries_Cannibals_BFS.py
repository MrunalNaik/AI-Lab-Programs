from collections import deque

class State:
    def __init__(self, m, c, boat):
        self.m = m
        self.c = c
        self.boat = boat

    def __eq__(self, other):
        return self.m == other.m and self.c == other.c and self.boat == other.boat

    def __hash__(self):
        return hash((self.m, self.c, self.boat))


# Possible moves for boat capacity = 2
moves = [
    (1, 0),   # One missionary
    (2, 0),   # Two missionaries
    (0, 1),   # One cannibal
    (0, 2),   # Two cannibals
    (1, 1)    # One missionary and one cannibal
]


def is_valid(state):

    if state.m < 0 or state.m > total_m:
        return False

    if state.c < 0 or state.c > total_c:
        return False

    # Left bank
    if state.m > 0 and state.c > state.m:
        return False

    # Right bank
    rm = total_m - state.m
    rc = total_c - state.c

    if rm > 0 and rc > rm:
        return False

    return True


def bfs():

    queue = deque([start])
    visited = {start}
    parent = {}

    while queue:

        current = queue.popleft()

        if current == goal:

            path = []

            while current != start:
                path.append(current)
                current = parent[current]

            path.append(start)
            path.reverse()

            return path

        for m, c in moves:

            if current.boat == 'L':
                new_state = State(current.m - m, current.c - c, 'R')
            else:
                new_state = State(current.m + m, current.c + c, 'L')

            if is_valid(new_state) and new_state not in visited:

                visited.add(new_state)
                parent[new_state] = current
                queue.append(new_state)

    return None


# ---------------- MAIN ----------------

total_m = int(input("Enter number of missionaries: "))
total_c = int(input("Enter number of cannibals: "))
boat_capacity = int(input("Enter boat capacity: "))

if boat_capacity != 2:
    print("This program supports only boat capacity = 2")
    exit()

start = State(total_m, total_c, 'L')
goal = State(0, 0, 'R')

solution = bfs()

if solution:

    print("\nSolution found in", len(solution)-1, "moves:\n")

    for i, state in enumerate(solution):

        lm = state.m
        lc = state.c

        rm = total_m - lm
        rc = total_c - lc

        print(
            f"Step/Level {i}: "
            f"Left [M={lm}, C={lc}] | "
            f"Boat on {state.boat} | "
            f"Right [M={rm}, C={rc}]"
        )

else:
    print("No Solution Found")