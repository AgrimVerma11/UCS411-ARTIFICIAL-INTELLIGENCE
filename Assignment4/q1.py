# 8 puzzle solved using Best First Search
# Heuristic h(n) = number of misplaced tiles compared to the goal state
import heapq

start = (2, 0, 3,
         1, 8, 4,
         7, 6, 5)

goal = (1, 2, 3,
        8, 0, 4,
        7, 6, 5)


def misplaced(state):
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:   # blank is not counted
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


def best_first(start, goal):
    # priority queue is ordered only by the heuristic value (greedy)
    pq = [(misplaced(start), start, [start])]
    visited = set()
    while pq:
        h, state, path = heapq.heappop(pq)
        if state == goal:
            return path
        if state in visited:
            continue
        visited.add(state)
        for nxt in neighbours(state):
            if nxt not in visited:
                heapq.heappush(pq, (misplaced(nxt), nxt, path + [nxt]))
    return None


path = best_first(start, goal)
print("Best First Search solution\n")
for step in path:
    show(step)
print("Total moves =", len(path) - 1)
