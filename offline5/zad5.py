# Jakub Kroczek
# Tworzę kolejkę priorytetową w której umieszczam przystanki od najwiekszej ilosci ropy do najmniejszej z zasięgu na
# jaki mozemy dojechac (od 0 do suma). W petli while pozyskuje i zapisuję w tablicy najlepsze przystanki ktore zapewnią
# najwiekszy zasięg przy najmniejszej ilosci przystanków. Na końcu sortuję przystanki w kojeności od pierwszego
# przystanku do ostatniego
# złożoność czasowa: n*log(n)
# złożoność pamięciowa: n
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