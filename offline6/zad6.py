import collections

from zad6testy import runtests

def longer( G, s, t ):
    tab=[]
    tab1=[]
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
            elif G[u][i]==t and wierzcholki[u].d==wierzcholki[t].d-1:
                wierzcholki.append(wierzcholek())
                wierzcholki[-1].visited=True
                wierzcholki[-1].d=wierzcholki[u].d+1
                wierzcholki[-1].parent=u
    x=t
    while wierzcholki[x].parent!=None:
        tab.append([x, wierzcholki[x].parent])
        x=wierzcholki[x].parent
    for i in range(len(G), len(wierzcholki)):
        if [t, wierzcholki[i].parent] in tab:
            tab1.append([t, wierzcholki[i].parent])
        x = wierzcholki[i].parent
        while wierzcholki[x].parent!=None:
            if [x, wierzcholki[x].parent] in tab:
                tab1.append([x, wierzcholki[x].parent])
            x = wierzcholki[x].parent
        tab = tab1.copy()
        tab1 = []
    if len(tab)==0:
        return None
    return tab[0]
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )