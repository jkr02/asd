# Jakub Kroczek
# Tworzę macierz n*n (n=liczba lotnisk) gdzie pod dane indeksy wpisuję najtańszy przejazd pomiedzy wszystkimi dwoma punktami
# następnie algorytmem Dijkstry szukam najkrótszej ścieżki pomiedzy punktem "s" i "t"
# zlozonosc czasowa: n^2
# zlozonosc pamieciowa n^2
import collections

from kol3btesty import runtests
def airports( G, A, s, t ):
    # tu prosze wpisac wlasna implementacje
    def Dijkstra(Graf, p, k):
        nonlocal n
        d = [float("inf") for _ in range(n)]
        pop = [None for _ in range(n)]
        d[p]=0
        Q=collections.deque()
        for i in range(n):
            Q.append(i)
        while Q:
            u = Q.popleft()
            for v in range(n):
                if v==u:
                    continue
                if d[v]>d[u]+Graf[u][v]:
                    d[v]=d[u]+Graf[u][v]
                    pop[v]=u
        return d[k]


    n=len(A)
    N=len(G)
    macierz=[[float("inf") for _ in range(n)]for _ in range(n)]
    for i in range(N):
        for j in range(len(G[i])):
            macierz[i][G[i][j][0]] = G[i][j][1]
            macierz[G[i][j][0]][i] = G[i][j][1]
    for i in range(n):
        for j in range(i+1, n):
            if A[i]+A[j]<macierz[i][j]:
                macierz[i][j]=A[i]+A[j]
                macierz[j][i]=A[i]+A[j]
    return Dijkstra(macierz, s, t)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( airports, all_tests = True )