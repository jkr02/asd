import collections

print(float('inf'))
if 6<float('inf'):
    print("tso")
def BFS(a, b, tablica, parent, n):
    visited=[False for _ in range(n)]
    q=collections.deque()
    visited[a]=True
    q.append(a)
    while q:
        v=q.popleft()
        for u in range(n):
            if not visited[u] and tablica[v][u]>0:
                visited[u]=True
                q.append(u)
                parent[u]=v
    if visited[b]:
        return True
    return False
def edmonds_karp(tablica, a, b, n):
    parent = [-1 for _ in range(n)]
    maxflow=0
    while BFS(a, b, tablica, parent, n):
        pathflow=float("inf")
        z = a
        while z!=b:
            pathflow=min(pathflow, tablica[parent[z]][z])
            z = parent[z]
        maxflow+=pathflow
        z = a
        while z!=b:
            tablica[parent[z]][z]-=pathflow
            tablica[z][parent[z]]+=pathflow
            z=parent[z]
    return maxflow
