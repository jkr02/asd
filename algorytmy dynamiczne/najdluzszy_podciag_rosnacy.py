T = [1, 2, 1, 4, 3, 3, 2, 1, 5, 6, 7]

def NPR(T):
    n=len(T)
    tab=[1 for _ in range(n)]
    for i in range(n):
        maximum=0
        for j in range(i):
            if T[j]<T[i] and maximum<tab[j]:
                maximum=tab[j]
        tab[i] = maximum + 1
    return max(tab)
print(NPR(T))