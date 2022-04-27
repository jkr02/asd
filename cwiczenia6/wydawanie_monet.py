T=[1, 2, 5, 10, 20, 50, 100, 200, 500]
p=19
n=len(T)
tab=[[[0] for _ in range(p+1)] for _ in range(n+1)]
for x in range(1, n):
    if T[x]<=p:
        tab[x][T[x]][0]=1
        tab[x][T[x]].append(T[x])
        for y in range(1, n+1-T[x]):
            if tab[x-1][y][0]!=0:
                if tab[x][y][0]+1<tab[x-1][y+T[x]][0]:
                    tab[x][y+T[x]]=tab[x][y].copy()
                    tab[x][y + T[x]].append(x)
            else:
