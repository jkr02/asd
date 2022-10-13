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
    """macierz sąsiedztwa
    dobry dla grafów rzadkich
    tylko dodatnie wagi krawedzi
    E*log(V)"""
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
    """reprezentacja macierzowa
    może zawierać dodatnie i ujemne wagi
    nie moze zaawierac ujemnych cykli
    czas: V^3
    pam: V^2"""
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
    """reprezentacja macierzy sąsiedztwa
    dla grafów z dodatnimi i ujemnymi wagami
    bez ujemnych cyklów
    najkrótsze ścieżki z źródła do reszty wierzchołków
    V^2*E"""
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
####################################################
def Dijkstra_1(G, s):
    n=len(G)
    d=[float("inf")]*n
    parents = [None]*n
    d[s]=0
    q=PriorityQueue()
    q.put((0, s))
    visited = [False]*n
    while not q.empty():
        distance, u = q.get()
        if visited[u] == True:
            continue
        visited[u]=True
        for v, w in G[u]:
            relax(d, parents, u, v, w)
            q.put((d[v], v))
    return d
# graph = [[(1, 7), (2, 5)], [], [(3, 4), (1, 8)], [(0, 5), (2, 4)]]
# print(Dijkstra_1(graph, 0))
def Bellman_ford_1(G, s):
    n=len(G)
    d=[float("inf")]*n
    parent=[None]*n
    d[s]=0
    for i in range(n-1):
        for u in range(n):
            for v, w in G[u]:
                relax(d, parent, u, v, w)
    for u in range(n):
        for v, w in G[u]:
            if d[v]<=d[u]+w:
                continue
            else:
                return d, False
    return d, True
graph = [[(1, 10)], [(2, 20)], [(3, 9)], [(2, 20)]]
print(Dijkstra_1(graph, 0))
