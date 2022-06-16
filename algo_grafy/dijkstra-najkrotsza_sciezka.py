from queue import PriorityQueue
def shortest_path(G, s):
    q = PriorityQueue()
    prev=[-1 for _ in G]
    dist=[float('inf') for _ in G]
    prev[s]=0
    q.put((0, s))
    while not q.empty():
        d, v = q.get()
        for p, w in G[v]:
            if dist[p]>d+w:
                dist[p]=d+w
                q.put((d+w, p))
    return dist, prev
#ALBO 1:inf dodatnie
def dijkstra(G, s):
    n = len(G)
    distances = [float("inf") for _ in range(n)]
    parents = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    q = PriorityQueue()
    distances[s] = 0
    q.put((0, s))
    while not q.empty():
        r, t = q.get()
        if visited[t]:
            continue
        else:
            visited[t] = True
        for u, w in G[t]:
            if parents[t] != u:
                relax(distances, parents, t, u, w)
                q.put((distances[u], u))
    return distances
def relax(d, parents, u, v, w):
    if d[v] > d[u] + w:
        d[v] = d[u] + w
        parents[v] = u
#albo INF:INF
def floyd_warshall(G):
    n = len(G)
    D = [row.copy() for row in G]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]
    return D
# 1:inf
def bellman_ford(G, s):
    n = len(G)
    distances = [float("inf") for _ in range(n)]
    parents = [None for _ in range(n)]
    distances[s] = 0

    for _ in range(1, n - 1):
        for v in range(n):
            for u, w in G[v]:
                relax(distances, parents, u, v, w)

    for v in range(n):
        for u, w in G[v]:
            if distances[v] <= distances[u] + w:  # cykl o wadze ujemnej
                continue
            else:
                return distances, False

    return distances, True
def relax(d, parents, u, v, w):
    if d[v] > d[u] + w:
        d[v] = d[u] + w
        parents[v] = u
