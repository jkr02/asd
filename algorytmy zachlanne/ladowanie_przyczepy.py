T = [2, 2, 4, 8, 1, 8, 16]
K = 27
def ladowanie_przyczepy(T, K):
    T.sort(reverse=True)
    n = len(T)
    licznik = 0
    for x in range(n):
        if K >= T[x]:
            K -= T[x]
            licznik += 1
    return licznik
print(ladowanie_przyczepy(T, K))