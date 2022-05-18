from random import randint
T = [randint(1, 100) for _ in range(randint(100000, 100100))]
print(len(T))
def min_k(T, k):
    n=len(T)
    tab=[0 for _ in range(n)]
    for i in range(k):
        tab[i]=T[i]
    for i in range(k, n):
        minimum=tab[i-k]
        for j in range(i-k+1, i):
            if minimum>tab[j]:
                minimum=tab[j]
        tab[i]=minimum+T[i]
    minimum=tab[n-k]
    for i in range(n-k+1, n):
        if minimum>tab[i]:
            minimum=tab[i]
    return minimum
print(min_k(T, 100))