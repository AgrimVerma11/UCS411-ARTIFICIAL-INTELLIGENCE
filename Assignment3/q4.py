# Finding the depth at which the goal is reached using Iterative Deepening Search
# Initial: A alone on the table, C sitting on top of B
# Goal:    one tower  A (bottom) - B - C (top)


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


def dls(state, goal, limit, path):
    if state == goal:
        return True
    if limit == 0:
        return False
    for nxt in successors(state):
        if nxt not in path:
            if dls(nxt, goal, limit - 1, path + [nxt]):
                return True
    return False


start = canon([["A"], ["B", "C"]])
goal = canon([["A", "B", "C"]])

# keep increasing the depth limit until the goal is found
depth = 0
while True:
    print("Trying depth limit =", depth)
    if dls(start, goal, depth, [start]):
        print("\nGoal achieved at depth =", depth)
        break
    depth += 1
