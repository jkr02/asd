def dijkstra_matrix(graph, start):
    """reprezentacja macierzowa
    V^2"""
    n=len(graph)
    visited = [False for _ in range(n)]
    d = [float("inf") for _ in range(n)]
    d[start] = 0
    while True:
        shortest_distance = float("inf")
        shortest_index = -1
        for i in range(n):
            if d[i] < shortest_distance and not visited[i]:
                shortest_distance = d[i]
                shortest_index = i
        if shortest_index == -1:
            return d
        for i in range(n):
            if graph[shortest_index][i] != 0 and d[i] > d[shortest_index] + graph[shortest_index][i]:
                d[i] = d[shortest_index] + graph[shortest_index][i]
        visited[shortest_index] = True