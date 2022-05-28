# Jakub Kroczek
# W programie najpierw sprawdzam czy w grafie są liście (jedna brama prowadzi do nikad) to oznacza ze nie ma takiej
# sciezki (zwraca NONE)
# Nastepnie sprawdzam czy graf jest spojny jezeli nie to nie ma takiej sciezki (zwaca NONE)
# I co dopiero teraz sprawdzam czy isnieje taka sciezka zmodyfikowanym dfs (zaczyna od wierzchołka 0 i wychodzi
# przez bramę o indeksie 0, nastepnie sprawdzam w głąb kolejne wierzcholki z przeciwnej bramy aniezeli weszlismy, jezeli
# bylismy to nie odwiedzamy, jezeli nie bylismy to wchodzimy itd. jezeli dlugosc w glab wynosci tyle co liczba miast,
# to sprawdzamy czy da sie przejsc do miasta 0 od jego drugiej bramy szukamy poki nie znajdzie [zwraca sciezke],
# jezeli nie znajdzie wsrod wszystkich mozliwosci to zwraca NONE)
# zlozonosc czasowa: V!
# zlozonosc obliczeniowa: V^2
import collections
from zad7testy import runtests

def droga( G ):
    n=len(G)
    def spojny(G):
        nonlocal n
        class w:
            def __init__(self):
                self.visit=False
        t=[w() for _ in range(n)]
        P=collections.deque()
        P.append(0)
        while P:
            u=P.popleft()
            for v in G[u][0]:
                if not t[v].visit:
                    t[v].visit=True
                    P.append(v)
            for v in G[u][1]:
                if not t[v].visit:
                    t[v].visit=True
                    P.append(v)
        for i in range(n):
            if not t[i].visit:
                return False
        return True
    def lisc(G):
        nonlocal n
        for i in range(n):
            if len(G[i][0])==0 or len(G[i][1])==0:
                return True
        return False

    def modify_dfs(s, d):
        nonlocal tab, G, visited, n, parents, gates
        visited[s]=True
        if d==n:
            if gates[s][parents[s]]!=0:
                if gates[s][0]==0:
                    if gates[0][s]==1:
                        tab.append(s)
                        return True
            else:
            #elif gates[s][parents[s]]!=1:
                if gates[s][0]==1:
                    if gates[0][s]==1:
                        tab.append(s)
                        return True
            visited[s]=False
            return False
        if gates[s][parents[s]]!=0:
            for i in range(len(G[s][0])):
                if not visited[G[s][0][i]]:
                    parents[G[s][0][i]]=s
                    if modify_dfs(G[s][0][i], d+1):
                        tab.append(s)
                        return True
        else:
        #elif gates[s][parents[s]]!=1:
            for i in range(len(G[s][1])):
                if not visited[G[s][1][i]]:
                    parents[G[s][1][i]] = s
                    if modify_dfs(G[s][1][i], d+1):
                        tab.append(s)
                        return True
        visited[s]=False
        return False
    if not spojny(G):
        return None
    if lisc(G):
        return None
    visited = [False for _ in range(n)]
    parents = [-1 for _ in range(n)]
    tab = []
    gates = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in G[i][0]:
            gates[i][j]=0
        for j in G[i][1]:
            gates[i][j]=1
    parents[0]=G[0][1][0]
    if modify_dfs(0, 1):
        return tab[::-1]
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( droga, all_tests = True )