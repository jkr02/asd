def dijkstra_matrix(graph, start):
    n=len(graph)
    visited = [False for _ in range(n)]
    distances = [float("inf") for _ in range(n)]
    distances[start] = 0
    while True:
        shortest_distance = float("inf")
        shortest_index = -1
        for i in range(n):
            if distances[i] < shortest_distance and not visited[i]:
                shortest_distance = distances[i]
                shortest_index = i
        if shortest_index == -1:
            return distances
        for i in range(n):
            if graph[shortest_index][i] != 0 and distances[i] > distances[shortest_index] + graph[shortest_index][i]:
                distances[i] = distances[shortest_index] + graph[shortest_index][i]
        visited[shortest_index] = True