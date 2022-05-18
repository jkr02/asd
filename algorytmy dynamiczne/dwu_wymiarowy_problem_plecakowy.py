import time
from random import randint
T = [[randint(1, 100), randint(1, 100), randint(1, 100)] for _ in range(randint(10000, 50000))]
print(len(T))
H=20
W=30
start=time.time()
def dwpp(T, H, W):
    n=len(T)
    tab = [[[0 for _ in range(W+1)] for _ in range(H+1)] for _ in range(n)]
    for i in range(n):
        for h in range(H+1):
            for w in range(W+1):
                if h>=T[i][1] and w>= T[i][2]:
                    tab[i][h][w]=max(tab[i-1][h][w], tab[i-1][h-T[i][1]][w-T[i][2]]+T[i][0])
                else:
                    tab[i][h][w]=tab[i-1][h][w]
    return tab[n-1][H][W]
print(dwpp(T, H, W))
stop=time.time()
print(stop-start)


