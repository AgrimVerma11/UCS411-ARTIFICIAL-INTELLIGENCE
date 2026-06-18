# Blocks world problem solved using Depth First Search (DFS)

# A state is kept as a tuple of stacks, each stack written bottom -> top.
# Initial: A is alone on the table, C is sitting on top of B
# Goal:    one tower  A (bottom) - B - C (top)


def canon(stacks):
    # drop empty stacks and keep a fixed order so equal states match
    return tuple(sorted(tuple(s) for s in stacks if s))


def successors(state):
    result = []
    stacks = [list(s) for s in state]
    for i in range(len(stacks)):
        block = stacks[i][-1]              # only the top block is free to move
        # move the block onto the table as a new stack
        if len(stacks[i]) > 1:
            new = [list(s) for s in stacks]
            new[i].pop()
            new.append([block])
            result.append(canon(new))
        # move the block on top of another stack
        for j in range(len(stacks)):
            if i != j:
                new = [list(s) for s in stacks]
                new[i].pop()
                new[j].append(block)
                result.append(canon(new))
    return result


def show(state):
    print(" , ".join("-".join(s) for s in state))


def dfs(start, goal):
    stack = [(start, [start])]            # frontier used like a LIFO stack
    visited = set()
    while stack:
        state, path = stack.pop()
        if state == goal:
            return path
        if state in visited:
            continue
        visited.add(state)
        for nxt in successors(state):
            if nxt not in visited:
                stack.append((nxt, path + [nxt]))
    return None


start = canon([["A"], ["B", "C"]])
goal = canon([["A", "B", "C"]])

path = dfs(start, goal)
print("DFS solution (", len(path) - 1, "moves):\n")
for step in path:
    show(step)
