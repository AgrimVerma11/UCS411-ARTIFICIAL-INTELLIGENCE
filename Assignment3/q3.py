# Blocks world problem solved using Depth Limited Search with depth limit = 1
# Initial: B alone on the table, C sitting on top of A
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


def show(state):
    return " , ".join("-".join(s) for s in state)


def dls(state, goal, limit, path):
    if state == goal:
        return True
    if limit == 0:
        return False
    for nxt in successors(state):
        if nxt not in path:               # don't revisit nodes on this path
            if dls(nxt, goal, limit - 1, path + [nxt]):
                return True
    return False


start = canon([["B"], ["A", "C"]])
goal = canon([["A", "B", "C"]])

limit = 1
print("Start:", show(start))
print("Goal :", show(goal))
print()
print("States reachable within depth", limit, ":")
for s in successors(start):
    print(" ", show(s))
print()

found = dls(start, goal, limit, [start])
if found:
    print("Goal reached within depth 1 -> search is complete")
else:
    print("Goal NOT reached within depth 1 -> search is incomplete for depth = 1")
