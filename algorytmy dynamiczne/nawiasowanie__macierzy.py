def NM(lista):
    n=len(lista)
    m = [[0 for _ in range(n)] for _ in range(n)]
    s = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(1, n):
        for j in range(n-i):
            l=j+i
            if j<l-2:
                m[j][l]
            for k in range(j, l-1):
                q=m[j][k]+m[k+1][j]+(len(lista[j-1])*len(lista[k])*len(lista[l]))
                if q<m[j][l]:
                    m[j][l]=q
                    s[j][l]=k
    return m, s