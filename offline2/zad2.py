# Jakub Kroczek
# Na początku Merge-Sort po pierwszej współrzędnej przedziału rosnąco, a gdy pierwsze wpółrzędne
# są takie same to po drugiej współrzędnej malejąco
# Następnie jest sprawdzanie dla każdego elementu (który się nie zawiera w żadnym innym i binarne szukanie elementu
# do którego warto sprawdzać czy się będzie zawierał w przedziale, który jest określony przez pierwszą pętlę for)
# ile elementów się w nim zawiera
# Algorytm jest poprawny, gdyż po posortowaniu algorytm przechodzi w pierwszej pętli tylko po elementach, które nie
# zawierają się w innych elementach. Elementy, które warto sprawdzić dla elementu z pierwszej pętli to takie, których
# pierwsza współrzędna przedziału jest mniejsza (bądź równa dla przedziałów [x, x]) od drugiej współrzędnej pierwszego
# elementu, gdyż pozostałe się nie będą w nim zawierać. Nie warto również sprawdzać elementów, których liczba elementów
# pomiedzy nim, a takim elementem jak w poprzednim zdaniu, jest mniejsza, bądź równa tymczasowej największej liczebności
# zbiorów w zbiorze
# Złożoność obliczeniowa: nlog(n) + n^2


from zad2testy import runtests


def depth(L):
    # tu prosze wpisac wlasna implementacje
    def wyszukiwanie_binarne(i, a):
        left = i
        right = n-1
        while left <= right:
            index = (left+right)//2
            if L[index][0] < a:
                left = index+1
            elif L[index][0] > a:
                right = index-1
            else:
                return index
        return left
    def merge_sort(tab):
        n = len(tab)
        if n > 1:
            mid = n//2
            l = tab[:mid]
            r = tab[mid:]
            d_l = len(l)
            d_r = len(r)
            merge_sort(l)
            merge_sort(r)
            i=0
            j=0
            k=0
            while i < d_l and j < d_r:
                if l[i][0] < r[j][0]:
                    tab[k] = l[i]
                    i+=1
                elif l[i][0] > r[j][0]:
                    tab[k] = r[j]
                    j+=1
                elif l[i][0] == r[j][0] and l[i][1] > r[j][1]:
                    tab[k] = l[i]
                    i+=1
                else:
                    tab[k]=r[j]
                    j+=1
                k+=1
            while i < d_l:
                tab[k] = l[i]
                i+=1
                k+=1
            while j < d_r:
                tab[k] = r[j]
                j+=1
                k+=1
    merge_sort(L)
    n = len(L)
    tab = [1 for _ in range(n)]
    max_g = 0
    p = 1
    for y in range(n):
        if tab[y]:
            liczba = 0
            p = wyszukiwanie_binarne(p, L[y][1] + 1)
            if p-y > max_g:
                for x in range(y+1, p):
                    if L[x][1] <= L[y][1]:
                        tab[x] = 0
                        liczba += 1
                if liczba > max_g:
                    max_g = liczba
    return max_g


runtests( depth ) 
