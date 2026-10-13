# Kruskal's Algorithm

# Graph edges: (weight, vertex1, vertex2)
edges = [
    (10, 'A', 'B'),
    (6, 'A', 'C'),
    (5, 'B', 'C'),
    (15, 'B', 'D'),
    (4, 'C', 'D'),
    (7, 'C', 'E'),
    (8, 'D', 'E')
]

# Sort edges by weight
edges.sort()

# Parent dictionary
parent = {
    'A': 'A',
    'B': 'B',
    'C': 'C',
    'D': 'D',
    'E': 'E'
}

# Find the parent of a vertex
def find(vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent[vertex])
    return parent[vertex]

# Join two sets
def union(v1, v2):
    root1 = find(v1)
    root2 = find(v2)

    if root1 != root2:
        parent[root2] = root1
        return True

    return False


# Kruskal's Algorithm
mst = []
total_cost = 0

for weight, v1, v2 in edges:
    if union(v1, v2):
        mst.append((v1, v2, weight))
        total_cost += weight

# Display Minimum Spanning Tree
print("Edges in Minimum Spanning Tree:")

for v1, v2, weight in mst:
    print(v1, "-", v2, ":", weight)

print("Total cost:", total_cost)