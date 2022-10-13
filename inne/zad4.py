def iamlate(T, V, q, l):
    n=len(V)
    if T[-1]+q<l:
        return []
    tab=[[(float("inf"), []) for _ in range(n)]for _ in range(q+1)]
    tab[0][0]=(0, [])
    for i in range(1, min(q, V[0])+1):
        tab[i][0]=(1, [0])
    for i in range(1, n):
        d=T[i]-T[i-1]
        if d>q:
            return []
        for j in range(d, q+1):
            tab[j-d][i]=tab[j][i-1]
        if tab[0][i][0]==float("inf"):
            return []
        k=0
        for a in range(q+1):
            if tab[a][i][0]==float("inf"):
                break
            k+=1
        for a in range(k):
            for b in range(min(V[i]+1, q+1-a)):
                if tab[b+a][i][0]>tab[a][i][0]+1:
                    tmp = tab[a][i][1].copy()
                    tmp.append(i)
                    tab[b+a][i]=(tab[a][i][0]+1, tmp)
        if l==T[i]:
            return tab[0][i][1]
    return tab[l-T[-1]][-1][1]
T=[0,1,2]
V=[2,1,5]
l=4
q=2
print(iamlate(T, V, q, l))


