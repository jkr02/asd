# f(i, j)-najmniejsza liczba postojów z największą ceną
# f(0, j)=T[0]
# f(i, j)=min(
import queue

from zad5testy import runtests

def plan(T):
    n=len(T)
    tab=[0]
    maxind=0
    suma=T[0]
    P=queue.PriorityQueue()
    while suma<n-1:
        for x in range(maxind+1, suma+1):
            P.put((-T[x], x))
        maksimum, indeks = P.get()
        maxind=suma
        suma-=maksimum
        tab.append(indeks)
    tab.sort()
    return tab
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )