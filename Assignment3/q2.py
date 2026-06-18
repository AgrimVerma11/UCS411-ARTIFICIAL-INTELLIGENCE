# Blocks world problem solved using Breadth First Search (BFS)
# Same problem as Q1 so the two searches can be compared.
from collections import deque


def canon(stacks):
    return tuple(sorted(tuple(s) for s in stacks if s))


def successors(state):
    result = []
    stacks = [list(s) for s in state]
    for i in range(len(stacks)):
        block = stacks[i][-1]
        if len(stacks[i]) > 1:
            new = [list(s) for s in stacks]
            new[i].pop()
            new.append([block])
            result.append(canon(new))
        for j in range(len(stacks)):
            if i != j:
                new = [list(s) for s in stacks]
                new[i].pop()
                new[j].append(block)
                result.append(canon(new))
    return result


def show(state):
    print(" , ".join("-".join(s) for s in state))


def bfs(start, goal):
    queue = deque([(start, [start])])     # frontier used like a FIFO queue
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        if state in visited:
            continue
        visited.add(state)
        for nxt in successors(state):
            if nxt not in visited:
                queue.append((nxt, path + [nxt]))
    return None


start = canon([["A"], ["B", "C"]])
goal = canon([["A", "B", "C"]])

path = bfs(start, goal)
print("BFS solution (", len(path) - 1, "moves):\n")
for step in path:
    show(step)

# Comparison with Q1:
# BFS searches level by level so it always returns the shortest solution
# (3 moves here). DFS dives deep first, so it can return a longer path and
# the order of states it visits is different, even though it uses less memory.
