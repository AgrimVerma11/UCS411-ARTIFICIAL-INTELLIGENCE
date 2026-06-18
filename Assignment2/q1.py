# 8 puzzle problem solved using A* search (Manhattan distance)
import heapq

start = (1, 2, 3,
         8, 0, 4,
         7, 6, 5)

goal = (2, 8, 1,
        0, 4, 3,
        7, 6, 5)

# store the goal position (row, col) of every tile so we can measure distance
goal_pos = {}
for i in range(9):
    goal_pos[goal[i]] = (i // 3, i % 3)


def manhattan(state):
    dist = 0
    for i in range(9):
        tile = state[i]
        if tile != 0:                 # blank is not counted
            r, c = i // 3, i % 3
            gr, gc = goal_pos[tile]
            dist += abs(r - gr) + abs(c - gc)
    return dist


def neighbours(state):
    moves = []
    blank = state.index(0)
    r, c = blank // 3, blank % 3
    # blank can move up, down, left or right
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            pos = nr * 3 + nc
            new_state = list(state)
            new_state[blank], new_state[pos] = new_state[pos], new_state[blank]
            moves.append(tuple(new_state))
    return moves


def solve(start, goal):
    # each entry: (f = g + h, g, state, path so far)
    open_list = [(manhattan(start), 0, start, [start])]
    visited = set()
    while open_list:
        f, g, state, path = heapq.heappop(open_list)
        if state == goal:
            return path
        if state in visited:
            continue
        visited.add(state)
        for nxt in neighbours(state):
            if nxt not in visited:
                new_g = g + 1
                heapq.heappush(open_list, (new_g + manhattan(nxt), new_g, nxt, path + [nxt]))
    return None


def show(state):
    for i in range(0, 9, 3):
        row = state[i:i + 3]
        print(" ".join(str(x) if x != 0 else "_" for x in row))
    print()


path = solve(start, goal)
print("Solved in", len(path) - 1, "moves\n")
for step in path:
    show(step)
