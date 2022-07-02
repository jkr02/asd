def fast_sort(tab, a):
    n = len(tab)
    t=[[] for _ in range(n)]
    for i in range(n):
        t[int(((tab[i]-1)*n)/a)].append(tab[i])
    for i in range(n):
