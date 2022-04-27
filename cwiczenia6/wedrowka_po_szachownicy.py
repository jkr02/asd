from random import randint
n=1000
tab=[[randint(1, 10) for _ in range(n)] for _ in range(n)]

for x in range(1, n):
    tab[0][x]+=tab[0][x-1]
    tab[x][0]+=tab[x-1][0]
for x in range(1, n):
    for y in range(1, n):
        tab[x][y]+=min(tab[x-1][y], tab[x][y-1])
print(tab[n-1][n-1])