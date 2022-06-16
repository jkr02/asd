def maxflow( G,s ):
    def BFS(a, b, tablica, parent):
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