from zad1testy import runtests


def chaos_index( T ):
    k=0
    n=len(T)
    a=0
    while True:
        a+=1
        do=0
        licznik=0
        for i in range(n-1):
            if T[i]>T[i+1]:
                T[i], T[i+1]=T[i+1], T[i]
                licznik+=1
                do=1
            else:
                if licznik>k:
                    k=licznik
                licznik=0
        if licznik>k:
            k=licznik
        if do==0:
            break
    if a-1>k:
        k=a-1
    return k


runtests( chaos_index )
