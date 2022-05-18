def nawiasowanie(T):
    n=len(T)
    tab=[[0 for _ in range(n)] for _ in range(n)]
    for d in range(1, n-1):
        for i in range(1, n-d):
            j=i+d
            tab[i][j]=tab[i][i]+tab[i+1][j]+T[i-1]*T[i]*T[j]
            for k in range(i+1, j):
                pom = tab[i][k] + tab[k+1][j] + T[i-1]*T[k]*T[j]
                if pom<tab[i][j]:
                    tab[i][j]=pom
    return tab[1][n-1]