# Uniform Cost Search from S to G on the given weighted graph
import heapq

# graph stored as adjacency list -> neighbour and edge cost (undirected)
graph = {
    "S": [("A", 1), ("B", 5), ("C", 15)],
    "A": [("S", 1), ("G", 10)],
    "B": [("S", 5), ("G", 5)],
    "C": [("S", 15), ("G", 5)],
    "G": [("A", 10), ("B", 5), ("C", 5)],
}


def ucs(start, goal):
    # priority queue ordered by the cost so far
    pq = [(0, start, [start])]
    visited = set()
    while pq:
        cost, node, path = heapq.heappop(pq)
        if node == goal:
            return cost, path
        if node in visited:
            continue
        visited.add(node)
        for neighbour, weight in graph[node]:
            if neighbour not in visited:
                heapq.heappush(pq, (cost + weight, neighbour, path + [neighbour]))
    return None, None


cost, path = ucs("S", "G")
print("Cheapest path:", " -> ".join(path))
print("Total cost:", cost)
