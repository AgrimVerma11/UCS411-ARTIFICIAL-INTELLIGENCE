# Water jug problem - 4 litre and 3 litre jug, need exactly 2 litres in the 4 litre jug
from collections import deque

cap1 = 4   # capacity of first jug
cap2 = 3   # capacity of second jug
goal = 2   # required amount in the 4 litre jug


def next_states(state):
    a, b = state
    states = []
    states.append((cap1, b))            # fill the 4 litre jug
    states.append((a, cap2))            # fill the 3 litre jug
    states.append((0, b))               # empty the 4 litre jug
    states.append((a, 0))               # empty the 3 litre jug

    # pour from jug1 into jug2
    pour = min(a, cap2 - b)
    states.append((a - pour, b + pour))

    # pour from jug2 into jug1
    pour = min(b, cap1 - a)
    states.append((a + pour, b - pour))

    return states


def solve():
    start = (0, 0)
    visited = set()
    queue = deque([[start]])            # BFS keeping the whole path
    while queue:
        path = queue.popleft()
        state = path[-1]
        if state[0] == goal:
            return path
        if state in visited:
            continue
        visited.add(state)
        for nxt in next_states(state):
            if nxt not in visited:
                queue.append(path + [nxt])
    return None


path = solve()
print("Steps to get exactly 2 litres in the 4 litre jug:\n")
for state in path:
    print("4 litre jug =", state[0], "| 3 litre jug =", state[1])
