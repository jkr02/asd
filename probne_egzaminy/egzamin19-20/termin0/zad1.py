from queue import PriorityQueue

def islands(G, A, B):
    n=len(G)
    def dijkstra(G, s):
        n = len(G)
        distances = [[float("inf"), float("inf"), float("inf")] for _ in range(n)]
        visited = [[False, False, False] for _ in range(n)]
        parents=[[None, None, None] for _ in range(n)]
        q = PriorityQueue()
        distances[s] = [0,0,0]
        q.put((0, s, 0))
        q.put((0, s, 1))
        q.put((0, s, 2))
        while not q.empty():
            r, t, k = q.get()
            if visited[t][k]:
                continue
            else:
                visited[t][k] = True
            for u, w in G[t]:
                if parents[t][k] != u and k!=find(w):
                    relax(distances, parents, t, u, w, k, find(w))
                    q.put((distances[u][find(w)], u, (find(w))))
        return distances
    def relax(d, parents, u, v, w, k, a):
        if d[v][a] > d[u][k] + w:
            d[v][a] = d[u][k] + w
            parents[v][a] = u
    def find(x):
        if x==1:return 0
        if x==5:return 1
        if x==8:return 2
    T=[[]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j]>0:
                T[i].append((j,G[i][j]))
    dystanse = dijkstra(T,A)
    d=min(dystanse[B])
    if d==float("inf"):
        return None
    return d
graf= [ [0,5,1,8,0,0,0 ],
[5,0,0,1,0,8,0 ],
[1,0,0,8,0,0,8 ],
[8,1,8,0,5,0,1 ],
[0,0,0,5,0,1,0 ],
[0,8,0,0,1,0,5 ],
[0,0,8,1,0,5,0 ] ]
print(islands(graf, 5, 2))