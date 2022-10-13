def dominance(P):
    def partition(t, p, r):
        x=t[r]
        i=p-1
        for j in range(p, r):
            if t[j][0]<x[0] or (t[j][0]==x[0] and t[j][1]<x[1]):
                i+=1
                t[i], t[j] = t[j], t[i]
        t[i+1], t[r] = t[r], t[i+1]
        return i+1
    def QuickSort(t, p, r):
        if p<r:
            q=partition(t, p, r)
            QuickSort(t, p, q-1)
            QuickSort(t, q+1, r)
    n=len(P)
    T=[(P[i][0], P[i][1], i) for i in range(n)]
    QuickSort(T, 0, n-1)
    result=[T[0][2]]
    makind=0
    for i in range(n):
        if T[makind][1]>T[i][1]:
            makind=i
            result.append(T[i][2])
    return result
tab=[(2,2),(1,1),(2.5,0.5),(3,2),(0.5,3)]
print(dominance(tab))