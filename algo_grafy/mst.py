def kruskal(G, n):
    G.sort(key=lambda e: e[2])
    A = [Node(x) for x in range(n)]
    res = []
    for e in G:
        n1 = A[e[0]]
        n2 = A[e[1]]
        if not contains_cycle(n1, n2):
            res.append(e)
    return res
def contains_cycle(n1,n2):
    first = find(n1)
    second = find(n2)
    if first != second:
        union(first, second)
        return False
    else:
        return True
class Node:
    def __init__(self, value):
        self.value = value
        self.parent = self
        self.rank = 0  # oszacowanie na rozmiar zbioru / wysokość drzewa
def find(x):
    """znajdz reprezentanta zbioru do którego należy dany element"""
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent
def union(x, y):
    """połącz dwa zbiory"""
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
        if x.rank == y.rank:
            x.rank += 1
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1
##################################################
from queue import PriorityQueue
def prims(G):
    n = len(G)
    q = PriorityQueue()
    q.put((0, 0))
    visited = [False for _ in range(n)]
    parents = [None for _ in range(n)]
    weights = [float("inf") for _ in range(n)]
    weights[0] = 0
    while not q.empty():
        r, t = q.get()
        if visited[t]:
            continue
        else:
            visited[t] = True
        for u, w in G[t]:
            if weights[u] > w and parents[t] != u:
                weights[u] = w
                parents[u] = t
                q.put((w, u))
    res = []
    for i in range(1, n):
        weight = 0
        for e in G[i]:
            j, w = e
            if j == parents[i]:
                weight = w
                break
        res.append([parents[i], i, weight])
    return res