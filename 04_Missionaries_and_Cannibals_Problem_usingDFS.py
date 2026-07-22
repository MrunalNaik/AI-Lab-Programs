#Initial State:(Missionaries Left, Cannibals Left, Boat Position)
#initial_state = (3, 3, 'left')  # 3 missionaries, 3 cannibals, boat on the left bank

#goal_state = (0, 0, 'right')  # Goal state: all missionaries and cannibals on the right bank

class State:
    def __init__(self, m, c, boat):
        self.m = m
        self.c = c
        self.boat = boat

    def __eq__(self, other):
        return self.m == other.m and self.c == other.c and self.boat == other.boat

    def __hash__(self):
        return hash((self.m, self.c, self.boat))


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

    # Left Bank
    if state.m > 0 and state.c > state.m:
        return False

    # Right Bank
    rm = total_m - state.m
    rc = total_c - state.c

    if rm > 0 and rc > rm:
        return False

    return True


def dfs(state):

    if state == goal:
        path.append(state)
        return True

    visited.add(state)
    path.append(state)

    for m, c in moves:

        if state.boat == 'L':
            new_state = State(state.m - m, state.c - c, 'R')

        else:
            new_state = State(state.m + m, state.c + c, 'L')

        if is_valid(new_state) and new_state not in visited:

            if dfs(new_state):
                return True

    path.pop()
    return False


# ---------------- MAIN ----------------

total_m = int(input("Enter number of missionaries: "))
total_c = int(input("Enter number of cannibals: "))
boat_capacity = int(input("Enter boat capacity: "))

start = State(total_m, total_c, 'L')
goal = State(0, 0, 'R')

visited = set()
path = []

if dfs(start):

    print("\nSolution found in", len(path)-1, "moves:\n")

    for i, state in enumerate(path):

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