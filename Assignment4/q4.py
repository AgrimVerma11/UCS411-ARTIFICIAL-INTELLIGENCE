# AO* algorithm applied to the given AND-OR search tree
# Every edge has cost 1.

# estimated (heuristic) cost of the leaf nodes
heuristic = {
    "C": 12,
    "G": 5,
    "H": 7,
    "E": 4,
    "F": 4,
}

# Each internal node is stored with its connectors.
# A connector is a group of (child, edge_cost):
#   - a single child  -> an OR choice
#   - many children   -> an AND group (every child has to be solved)
graph = {
    "A": [[("B", 1)], [("C", 1)], [("D", 1)]],   # OR : reach A through B or C or D
    "B": [[("G", 1), ("H", 1)]],                  # AND: B needs both G and H
    "D": [[("E", 1), ("F", 1)]],                  # AND: D needs both E and F
}


def ao_star(node):
    # a leaf node simply returns its heuristic value
    if node not in graph:
        return heuristic[node], [node]

    best_cost = None
    best_path = None
    for connector in graph[node]:
        cost = 0
        path = [node]
        for child, edge in connector:
            child_cost, child_path = ao_star(child)
            cost += edge + child_cost
            path += child_path
        if best_cost is None or cost < best_cost:
            best_cost = cost
            best_path = path
    return best_cost, best_path


print("Cost of solving each child of A:")
for node in ["B", "C", "D"]:
    print(" ", node, "=", ao_star(node)[0])
print()

cost, path = ao_star("A")
print("Minimum cost from A =", cost)
print("Chosen solution nodes:", " ".join(path))
