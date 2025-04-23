def floyd_warshall(graph):
    n = len(graph)
    dist = [[graph[i][j] for j in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (dist[i][j] > dist[i][k]+dist[k][j]):
                    dist[i][j] = dist[i][k]+dist[k][j]
    return dist
graph = [
    [0, 3, float('inf'), float('inf')],
    [2, 0, float('inf'), 4],
    [float('inf'), 1, 0, 5],
    [float('inf'), float('inf'), 2, 0]
]

shortest_paths = floyd_warshall(graph)
print("All Pair Shortest Paths:")
for row in shortest_paths:
    print(row)