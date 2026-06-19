# 8 puzzle using Hill Climbing search
# Heuristic h(n) = number of misplaced tiles compared to the goal state
start = (2, 8, 3,
         1, 5, 4,
         7, 6, 0)

goal = (1, 2, 3,
        8, 0, 4,
        7, 6, 5)


def misplaced(state):
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1
    return count


def neighbours(state):
    moves = []
    blank = state.index(0)
    r, c = blank // 3, blank % 3
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            pos = nr * 3 + nc
            new = list(state)
            new[blank], new[pos] = new[pos], new[blank]
            moves.append(tuple(new))
    return moves


def show(state):
    for i in range(0, 9, 3):
        print(" ".join(str(x) if x != 0 else "_" for x in state[i:i + 3]))
    print()


def hill_climbing(start, goal):
    current = start
    path = [current]
    while current != goal:
        # pick the neighbour with the least number of misplaced tiles
        best = min(neighbours(current), key=misplaced)
        if misplaced(best) >= misplaced(current):
            # no neighbour is better -> we are stuck on a local optimum
            return path, False
        current = best
        path.append(current)
    return path, True


path, solved = hill_climbing(start, goal)
print("Hill Climbing search\n")
for step in path:
    show(step)
    print("misplaced tiles =", misplaced(step))
    print()

if solved:
    print("Goal reached in", len(path) - 1, "moves")
else:
    print("Hill climbing got stuck at a local optimum, goal not reached.")
