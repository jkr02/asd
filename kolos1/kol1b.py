# Jakub Kroczek
# Tworze tablice, ktora dla każdego elementu zawiera indeks 0-dlugosc wyrazu, a pozostale indeksy - liczby wystapien
# liter w slowie
# Nastepnie tworze mniejsze tablice, które zawierają slowa o tej samej dlugosci a nastepnie je sortuje wzgledem indeksow
# (od indeksu=1, bo indeks=0, to dlugosc slowa)
# Na końcu sprawdzam, ktory anagram jest najpopularniejszy poprzez sprawdzanie ile takich samych tablic wystepuje
# na tej podstawie uwazam, ze moj algorytm jest poprawny
# zlozonosc czasowa pesymistyczna: nlog(n)
# zlozonosc pamieciowa: n

from kol1btesty import runtests

def f(T):
    def merge_sort(A, x):
        n=len(A)
        if n>1:
            mid=n//2
            l=A[:mid]
            p=A[mid:]
            merge_sort(l, x)
            merge_sort(p, x)
            dl=len(l)
            dp=len(p)
            i=j=k=0
            while i<dl and j<dp:
                if l[i][x] <= p[j][x]:
                    A[k] = l[i]
                    k+=1
                    i+=1
                else:
                    A[k] = p[j]
                    j+=1
                    k+=1
            while i<dl:
                A[k] = l[i]
                k += 1
                i += 1
            while j<dp:
                A[k] = p[j]
                j += 1
                k += 1
    def radix_sort(tablica):
        for x in range(1, 27):
            merge_sort(tablica, x)
    n=len(T)
    maxlen=0
    tab=[[0 for _ in range(27)] for x in range(n)]
    for x in range(n):
        d = len(T[x])
        if d>maxlen:
            maxlen=d
        tab[x][0] = d
        for y in range(d):
            tab[x][ord(T[x][y])-96] += 1
    t = [[] for _ in range(maxlen)]
    for x in range(n):
        t[tab[x][0]-1].append(tab[x])
    for x in range(maxlen):
        radix_sort(t[x])
    m_popular=0
    for x in range(maxlen):
        temp=0
        for y in range(1, len(t[x])):
            if t[x][y] == t[x][y-1]:
                temp+=1
            else:
                if temp>m_popular:
                    m_popular = temp
                temp=0
        if temp>m_popular:
            m_popular=temp
    return m_popular+1


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True )
