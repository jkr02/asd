# Jakub Kroczek
# na początek tworzę listę krawędzi i sortuję ją niemalejąco, potem tworzę dwa wskaźniki i=0 j=n-2 (bo zeby graf był
# spojny to musi mieć co najmniej n-1 krawędzi) i jeżeli graf jest spójny to sprawdzam różnicę pomiędzy
# długościami 'j' i 'i' jezeli mniejsza od dotychczasowej najmniejszej to nadpisuję, oraz zwiekszam 'i', jezeli graf
# nie jest spójny to zwiększam 'j', robię to dopóki j<n
# złożoność czasowa: n^4
# złożoność pamięciowa: n^2
import collections

from zad8testy import runtests

def highway( A ):
    n = len(A)
    if n<=2:
        return 0
    def dlugosc(a, b):
        c = ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
        if c == int(c):
            return int(c)
        return int(c)+1
    def bfs():
        nonlocal n, tab, t
        visited=[False for _ in range(n)]
        q=collections.deque()
        q.append(0)
        visited[0]=True
        while q:
            u=q.popleft()
            for v in t[u]:
                if not visited[v]:
                    q.append(v)
                    visited[v]=True
        if False in visited:
            return False
        return True
    tab = []
    for i in range(n):
        for j in range(i+1, n):
            tab.append([i, j, dlugosc(A[i], A[j])])
    tab.sort(key=lambda x: x[2])
    i=0
    j=n-2
    minimum = tab[-1][2]-tab[0][2]+1
    t = [[] for _ in range(n)]
    d=len(tab)
    for x in range(0, j + 1):
        t[tab[x][0]].append(tab[x][1])
        t[tab[x][1]].append(tab[x][0])
    while True:
        if minimum<tab[j][2]-tab[i][2]:
            t[tab[i][0]].pop(0)
            t[tab[i][1]].pop(0)
            i += 1
            continue
        if bfs():
            if minimum>tab[j][2]-tab[i][2]:
                minimum=tab[j][2]-tab[i][2]
            t[tab[i][0]].pop(0)
            t[tab[i][1]].pop(0)
            i+=1
            continue
        j+=1
        if j==d:
            break
        t[tab[j][0]].append(tab[j][1])
        t[tab[j][1]].append(tab[j][0])
    return minimum
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )