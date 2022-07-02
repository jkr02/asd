from zad3testy import runtests


def kintersect( A, k ):
    tab=[(i, A[i][0], A[i][1]) for i in range(len(A))]
    tab.sort(key=lambda x: -x[2])
    max_length=0
    if k==1:
        wynik=[0]
        for i in range(len(A)):
            if tab[i][2]-tab[i][1]>max_length:
                max_length=tab[i][2]-tab[i][1]
                wynik[0]=tab[i][0]
        return wynik
    wynik=[]
    for i in range(len(A)):
        curr=[tab[i][0]]
        for j in range(len(A)):
            if i!=j and tab[j][1]<=tab[i][1]<tab[j][2]:
                curr.append(tab[j][0])
                if len(curr)==k:
                    length=min(tab[i][2]-tab[i][1], tab[j][2]-tab[i][1])
                    if length>max_length:
                        max_length=length
                        wynik.clear()
                        wynik=[curr[i] for i in range(k)]
                    break
    return wynik

runtests( kintersect )