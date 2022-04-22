from zad4testy import runtests

def select_buildings(T,p):
    n=len(T)
    def Bubble_sort(T):
        n = len(T)
        indeksy=[x for x in range(n)]
        for y in range(n):
            for x in range(n - y - 1):
                if T[x][1] > T[x + 1][1]:
                    T[x], T[x + 1] = T[x + 1], T[x]
                    indeksy[x], indeksy[x+1] = indeksy[x+1], indeksy[x]
                elif T[x][1] >= T[x + 1][1] and T[x][2]<T[x+1][2]:
                    T[x], T[x + 1] = T[x + 1], T[x]
                    indeksy[x], indeksy[x + 1] = indeksy[x + 1], indeksy[x]
        return T, indeksy
    P, indeksy=Bubble_sort(T)
    tab = [[[0] for _ in range(p+1)] for _ in range(n+1)]
    for i in range(n):
        for j in range(p+1):
            if j>=P[i][3]:
                max_k=n
                max_sum=0
                for k in range(i-1, -1, -1):
                    if len(tab[k][j-P[i][3]])>1:
                        if P[tab[k][j-P[i][3]][-1]][2]<P[i][1] and tab[k][j-P[i][3]][0]>max_sum:
                            max_k=k
                            max_sum=tab[k][j-P[i][3]][0]
                if max_sum+(P[i][2]-P[i][1])*P[i][0]>tab[i-1][j][0]:
                    tab[i][j]=tab[max_k][j-P[i][3]][:]
                    tab[i][j].append(i)
                    tab[i][j][0]+=(P[i][2]-P[i][1])*P[i][0]
                else:
                    tab[i][j]=tab[i-1][j][:]
            else:
                tab[i][j]=tab[i-1][j][:]
    max_sum=0
    max_k=0
    for i in range(1, p+1):
        if max_sum<=tab[n-1][i][0]:
            max_k=i
            max_sum=tab[n-1][i][0]
    for i in range(1, len(tab[n-1][max_k])):
        tab[n-1][max_k][i] = indeksy[tab[n-1][max_k][i]]
    # tu prosze wpisac wlasna implementacje
    return tab[n-1][max_k][1:]

runtests( select_buildings )