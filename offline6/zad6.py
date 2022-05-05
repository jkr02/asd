import collections

from zad6testy import runtests

def longer( G, s, t ):
    Q = collections.deque()
    class wierzcholek:
        def __init__(self):
            self.d=0
            self.visited=False
            self.parent=None
    wierzcholki=[wierzcholek() for _ in range(len(G))]
    wierzcholki[s].visited=True
    Q.append(s)
    while len(Q)>0:
        u = Q.popleft()
        for i in range(len(G[u])):
            if not wierzcholki[G[u][i]].visited:
                wierzcholki[G[u][i]].visited=True
                wierzcholki[G[u][i]].d=wierzcholki[u].d+1
                wierzcholki[G[u][i]].parent=u
                Q.append(G[u][i])
    pop=[t]
    tmp=[]
    for i in range(wierzcholki[t].d, 0, -1):
        if len(pop) == 1:
            for x in range(len(G[pop[0]])):
                if wierzcholki[G[pop[0]][x]].d == i-1:
                    if not G[pop[0]][x] in tmp:
                        tmp.append(G[pop[0]][x])
            if len(tmp) == 1:
                return (pop[0], tmp[0])
        else:
            for j in range(len(pop)):
                for x in range(len(G[pop[j]])):
                    if wierzcholki[G[pop[j]][x]].d == i-1:
                        if not G[pop[j]][x] in tmp:
                            tmp.append(G[pop[j]][x])
        pop=tmp.copy()
        tmp=[]
    return None
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )