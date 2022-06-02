import collections
import copy
import time
from zad9testy import runtests

def maxflow( G,s ):
    def searching_algo_BFS(s, t, parent, tablica):
        nonlocal n
        visited = [False] * (n+1)
        queue = collections.deque()
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.popleft()
            for ind, val in enumerate(tablica[u]):
                if not visited[ind] and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
        return True if visited[t] else False
    def ford_fulkerson(tablica, source, sink):
        parent = [-1]*(n+1)
        max_flow = 0
        while searching_algo_BFS(source, sink, parent, tablica):
            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, tablica[parent[s]][s])
                s = parent[s]
            max_flow += path_flow
            v = sink
            while(v != source):
                u = parent[v]
                tablica[u][v] -= path_flow
                tablica[v][u] += path_flow
                v = parent[v]
        return max_flow



    n=0
    for i in range(len(G)):
        if G[i][0]>n:
            n=G[i][0]
        if G[i][1]>n:
            n=G[i][1]
    n+=1
    tab = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in G:
        tab[i[0]][i[1]]=i[2]
    # for i in range(n+1):
    #     print(tab[i])
    # print()
    maksimum=0
    for i in range(n):
        if i != s:
            tab[i][-1] = float('Inf')
            for j in range(i+1, n):
                if j != s:
                    if sum(tab[:-1][i]) + sum(tab[:-1][j]) <= maksimum:
                        tab[j][-1]=0
                    else:
                        tab[j][-1] = float('Inf')
                        t=copy.deepcopy(tab)
                        temp = ford_fulkerson(t, s, n)
                        if temp > maksimum:
                            maksimum = temp
                        tab[j][-1] = 0
            tab[i][-1] = 0
    return maksimum

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxflow, all_tests = True )