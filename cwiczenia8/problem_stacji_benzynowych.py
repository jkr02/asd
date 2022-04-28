#podpunkt b) szukamy najblizszej tanszej od obecnej i tankujemy tyle zeby do niej dojechac, jesli w maksymalnym zasiegu
# nie ma tanszej to tankujemy do pelna i jedziemy do najtanszej stacji z maksymalnego zasiegu i powtarzamy. Adwent
#

import time
from random import randint
T=[randint(0, 1) for _ in range(100)]
L=10
def liczba_tankowan_a(T, L):
    n=len(T)
    tab=[1, 0]
    while tab[-1]+L<n-1:
        jest=0
        for i in range(tab[-1]+L, tab[-1], -1):
            if T[i]==1:
                jest=1
                tab.append(i)
                tab[0]+=1
                break
        if jest==0:
            return [0]
    return tab[0]
start=time.time()
print(liczba_tankowan_a(T, 100))
stop=time.time()
print(stop-start)

