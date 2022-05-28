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