# Jakub Kroczek
# tworze klase, ktora zawiera najmniejsza dlugosc do poczatkowego wierzcholka 's', nastepnie algorytmem BFS szukam i
# zapisuje te dlugosci. Nastepnie sprawdzam od wierzcholka 't' jego sasiadow, ktorzy maja dlugosc do 's' rowna dlugosci
# od 't' do 's' - 1 i zapisuje wszytkie w tablicy, ktore spelniaja to zalozenie. nastepnie sprawdzam dla tych
# wierzcholkow podobnie jak dla 't', gdy w tablicy poprzednikow bedzie jeden element i w terazniejszej rowniez jeden
# element, to oznacza ze przez te krawedz przebiegaja wszystkie najktotsze sciezki z 's' do 't', jesli takiej nie
# znajdziemy to oznacza ze nie ma takiej krawedzi przez ktore przechodzily by wszystkie najkrotsze sciezki (trzeba
# zwrocic 'NONE')
# zlozonosc czasowa: G+V
# zlozonosc pamieciowa: G
import collections

from zad6testy import runtests

def longer( G, s, t ):
    Q = collections.deque()
    class wierzcholek:
        def __init__(self):
            self.d=0
            self.visited=False
    wierzcholki=[wierzcholek() for _ in range(len(G))]
    wierzcholki[s].visited=True
    Q.append(s)
    while Q:
        u = Q.popleft()
        for i in range(len(G[u])):
            if not wierzcholki[G[u][i]].visited:
                wierzcholki[G[u][i]].visited=True
                wierzcholki[G[u][i]].d=wierzcholki[u].d+1
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