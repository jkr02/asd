# Jakub Kroczek
# Algorytmem Edmondsa-Karpa szukam wierszcholka, w ktorym jest najwiekszy przeplyw, nastepnie drugi raz szukam
# algorytmem Edmondsa-Karpa drugi wierzchołek (na grafie juz z wykorzystanymi przeplywami z pierwszego wierzcholka) i
# zwracam sume przeplywu do pierwszego wierzcholka wraz z drugiego wierzcholka
# zlozonosc czasowa: V^3 + V^2*E^2
# zlozonosc pamieciowa: V^2
import collections
from zad9testy import runtests

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
    n=0
    for i in range(len(G)):
        if G[i][0]>n:
            n=G[i][0]
        if G[i][1]>n:
            n=G[i][1]
    n+=1
    tab = [[0 for _ in range(n)] for _ in range(n)]
    for i in G:
        tab[i[0]][i[1]]=i[2]
    maksimuma=0
    maxinda=0
    tabwin=[x[:] for x in tab]
    for i in range(n):
        if i != s:
            t=[x[:] for x in tab]
            temp = edmonds_karp(t, s, i)
            if temp > maksimuma:
                maksimuma = temp
                maxinda=i
                tabwin=[x[:] for x in t]
    maksimumb=0
    for i in range(n):
        if i != s and i!=maxinda:
            t=[x[:] for x in tabwin]
            temp = edmonds_karp(t, s, i)
            if temp > maksimumb:
                maksimumb = temp
    return maksimuma+maksimumb
runtests( maxflow, all_tests = True )