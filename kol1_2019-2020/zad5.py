def string_sort(T):
    n=len(T)
    d=len(T[0])
    for i in range(1, n):
        if len(T[i])>d:
            d=len(T[i])
    for i in range(d-1, -1, -1):
        tab = [[] for _ in range(27)]
        for j in range(n):
            if len(T[j]) > i:
                tab[ord(T[j][i])-96].append(T[j])
            else:
                tab[0].append(T[j])
        licznik = 0
        for j in range(27):
            for k in range(len(tab[j])):
                T[licznik] = tab[j][k]
                licznik+=1
T = ["abcd", "pap", "xdddd", "int", "abc", "apf"]
string_sort(T)
print(T)