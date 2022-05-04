import collections

from zad6testy import runtests

def longer( G, s, t ):
    flag=0
    print(len(G))
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
        #     if G[u][i] == t:
        #         flag=1
        #         break
        # if flag == 1:
        #     flag=0
        #     break
    print(wierzcholki[t].d)
    k=t
    # for i in range(wierzcholki[t].d):
    #     a=k
    #     k=wierzcholki[a].parent
    #     tab=G.copy()
    #     tab[a].remove(k)
    #     tab[k].remove(a)
    #     w = [wierzcholek() for _ in range(len(G))]
    #     P=collections.deque()
    #     w[s].visited=True
    #     P.append(s)
    #     while len(P)>0:
    #         u = P.popleft()
    #         for i in range(len(tab[u])):
    #             if not w[tab[u][i]].visited:
    #                 w[tab[u][i]].visited = True
    #                 w[tab[u][i]].d = w[u].d + 1
    #                 w[tab[u][i]].parent = u
    #                 P.append(tab[u][i])
    #     if w[t].visited==False:
    #         return (a, k)
    #     if w[t].d > wierzcholki[t].d:
    #         return (a, k)
    # return None
    for i in range(wierzcholki[t].d):
        a=k
        k=wierzcholki[a].parent
        G[a].remove(k)
        G[k].remove(a)
        w = [wierzcholek() for _ in range(len(G))]
        P=collections.deque()
        w[s].visited=True
        P.append(s)
        while len(P)>0:
            u = P.popleft()
            for i in range(len(G[u])):
                if not w[G[u][i]].visited:
                    w[G[u][i]].visited = True
                    w[G[u][i]].d = w[u].d + 1
                    w[G[u][i]].parent = u
                    P.append(G[u][i])
            #         if G[u][i] == t:
            #             flag=1
            #             break
            # if flag == 1:
            #     flag=0
            #     break
        if w[t].visited==False:
            return (a, k)
        if w[t].d > wierzcholki[t].d:
            return (a, k)
        G[a].append(k)
        G[k].append(a)
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )