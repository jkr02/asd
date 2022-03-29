from zad1testy import runtests

def Median(T):
    def Insertion_sort(tab):
        n = len(tab)
        for x in range(1, n):
            temp = tab[x]
            j = x - 1
            while j >= 0 and temp < tab[j]:
                tab[j + 1] = tab[j]
                j -= 1
            tab[j + 1] = temp
    # tu prosze wpisac wlasna implementacje
    n=len(T)
    t=[0 for _ in range(n*n)]
    i=0
    for x in range(n):
        for y in range(n):
            t[i] = T[x][y]
            i+=1
    Insertion_sort(t)
    i=0
    for x in range(n-1, 0, -1):
        for y in range(x-1, -1, -1):
            T[x][y] = t[i]
            i+=1
    for x in range(n):
        T[x][x]=t[i]
        i+=1
    for x in range(n-2, -1, -1):
        for y in range(n-1, x, -1):
            T[x][y] = t[i]
            i+=1
    return T

runtests( Median ) 
