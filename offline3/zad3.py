# Jakub Kroczek
# Program tworzy kubełki o długości 10, wsadzane są do niego watości i sortowane dla liczby elementów w kubełku <=100
# jest to insertion-sort, dla wiekszych merge-sort, nastepnie kolejne wartości z kubełków są wsadzane do listy
# Złożoność czasowa: pesymistyczna nlog(n)
# Złożoność pamięciowa: pesymistyczna n+k



from zad3testy import runtests

def SortTab(T,P):
    # tu prosze wpisac wlasna implementacje
    def Mergesort(tab):
        n = len(tab)
        if n>1:
            mid = n//2
            l = tab[:mid]
            r = tab[mid:]
            d_l = len(l)
            d_r = len(r)
            Mergesort(l)
            Mergesort(r)
            i = 0
            j = 0
            k = 0
            while i < d_l and j < d_r:
                if l[i] < r[j]:
                    tab[k] = l[i]
                    i+=1
                    k+=1
                else:
                    tab[k] = r[j]
                    j+=1
                    k+=1
            while i<d_l:
                tab[k] = l[i]
                i+=1
                k+=1
            while j<d_r:
                tab[k]= r[j]
                j+=1
                k+=1

    maksimum = int(max(T))
    minimum = int(min(T))
    B = [[] for _ in range((maksimum-minimum)//10+1)]
    for i in range(len(T)):
        B[(int(T[i])-minimum)//10].append(T[i])
    for x in range(len(B)):
        d = len(B[x])
        if d < 2:
            continue
        elif d < 100:
            for i in range(1, d):
                key = B[x][i]
                j = i - 1
                while j >= 0 and key < B[x][j]:
                    B[x][j + 1] = B[x][j]
                    j -= 1
                B[x][j + 1] = key
        else:
            Mergesort(B[x])
    x=0
    for i in range(len(B)):
        for j in range(len(B[i])):
            T[x] = B[i][j]
            x+=1
    return T

runtests( SortTab )