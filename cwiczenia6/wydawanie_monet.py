import time
from sys import maxsize
T=[1, 2, 5, 10, 20, 50, 100, 200, 500]
p=19
def wydawanie_monet(T, p):
    n=len(T)
    tab=[[[maxsize] for _ in range(p+1)] for _ in range(n+1)]
    for x in range(n+1):
        tab[x][0][0]=0
    for x in range(1, n+1):
        if T[x-1]<=p:
            for y in range(T[x-1]):
                tab[x][y]=tab[x-1][y].copy()
            tab[x][T[x-1]][0]=1
            tab[x][T[x-1]].append(T[x-1])
            for y in range(1, p+1-T[x-1]):
                if tab[x-1][T[x-1]+y][0]>tab[x][y][0]+1:
                    tab[x][T[x-1]+y]=tab[x][y].copy()
                    tab[x][T[x-1]+y][0]+=1
                    tab[x][T[x-1]+y].append(T[x-1])
                else:
                    tab[x][T[x-1]+y]=tab[x-1][T[x-1]+y].copy()
        else:
            for y in range(1, p+1):
                tab[x][y] = tab[x - 1][y].copy()
    return tab[-1][-1]
start=time.time()
print(wydawanie_monet(T, 25696))
stop=time.time()
print(stop-start)