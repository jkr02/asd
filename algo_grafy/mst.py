def kruskal(G, n):
    """reprezentacja krawedziowa
    znajdowanie mst - minimalne drzewo rozpinajace
    graf posortowany (krawedzie niemalejaco): E*log*(E, V) - odwrotnosc funkcji ackermana
    graf nieposortowany: Elog(V)"""
    G.sort(key=lambda x: x[2]) # Gdy posortowany można opuścić
    A = [Node(x) for x in range(n)]
    res = []
    for x in G:
        n1 = A[x[0]]
        n2 = A[x[1]]
        if not contains_cycle(n1, n2):
            res.append(x)
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
    """
    reprezentacja krawedziowa
    Elog(V)
    """
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
################################
def Kruscal(G, n):
    G.sort(key=lambda x: x[2])
    result = []
    t=[klasa(i) for i in range(n)]
    for e in G:
        a=znajdz(t[e[0]])
        b=znajdz(t[e[1]])
        if not ma_cykl(a, b):
            result.append((e[0], e[1]))
    return result
class klasa:
    def __init__(self, value):
        self.parent=self
        self.value=value
        self.rank=0
def znajdz(i):
    if i.parent!=i:
        i.parent=znajdz(i)
    return i.parent
def unia(x, y):
    x = znajdz(x)
    y = znajdz(y)
    if x.rank==y.rank:
        return
    if x.rank>y.rank:
        y.parent=x
    else:
        x.parent=y
        if x.rank==y.rank:
            y.rank+=1
def ma_cykl(x, y):
    x = znajdz(x)
    y = znajdz(y)
    if x==y:
        return True
    unia(x, y)
    return False