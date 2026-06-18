# Travelling Salesman Problem for the given 4 nodes graph
from itertools import permutations

n = 4

# distance matrix (row/col index 0 = node 1, index 1 = node 2, and so on)
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0],
]

start = int(input("Enter the starting node (1-4): "))
start_index = start - 1

# all the nodes we still have to visit
other = [i for i in range(n) if i != start_index]

best_cost = float("inf")
best_route = None

# try every possible order of visiting the remaining nodes
for perm in permutations(other):
    route = [start_index] + list(perm) + [start_index]
    cost = 0
    for i in range(len(route) - 1):
        cost += dist[route[i]][route[i + 1]]
    if cost < best_cost:
        best_cost = cost
        best_route = route

print("Minimum cost =", best_cost)
print("Best route:", " -> ".join(str(node + 1) for node in best_route))
