tab=[0.5, 0.24, 1.25, 1.4, 2.3]
def przedzialy(T):
    n=len(T)
    liczba=1
    koniec=T[0]+1
    for i in range(1, n):
        if T[i]>koniec:
            koniec=T[i]+1
            liczba+=1
    return liczba