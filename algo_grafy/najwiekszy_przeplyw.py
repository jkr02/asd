import collections
def BFS(a, b, tablica, parent):
    n=len(tablica)
    visited = [False for _ in range(n)]
    q = collections.deque()
    visited[a] = True
    q.append(a)
    while q:
        v = q.popleft()
        for u in range(n):
            if not visited[u] and tablica[v][u]>0:
                visited[u] = True
                q.append(u)
                parent[u] = v
    if visited[b]:
        return True
    return False
def edmonds_karp(tablica, a, b):
    """reprezentacja
    V*E^2"""
    n=len(tablica)
    parent = [-1 for _ in range(n)]
    maxflow = 0
    while BFS(a, b, tablica, parent):
        pathflow = float("inf")
        z = b
        while z != a:
            pathflow = min(pathflow, tablica[parent[z]][z])
            z = parent[z]
        maxflow += pathflow
        z = b
        while z != a:
            tablica[parent[z]][z] -= pathflow
            tablica[z][parent[z]] += pathflow
            z = parent[z]
    return maxflow


def FordFulkerson(graph, source, sink):
    """reprezentacja macierzowa
    E*maxflow"""
    n=len(graph)
    parent = [-1 for _ in range(n)]
    max_flow = 0
    while BFS(source, sink, graph, parent):
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return max_flow


