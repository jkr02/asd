from random import randint

T = [randint(-50, 50) for _ in range(randint(5, 7))]

def suma_dlugosci(T):
    n=len(T)
    T.sort()
    print(T)
    d=[]
    u=[]
    for x in range(n):
        if T[x]<0:
            u.append(T[x])
        else:
            d.append(T[x])
    if len(u)>len(d):
        return u[(len(d)-len(u))//2]
    else:
        return d[(len(d)-len(u))//2]
print(suma_dlugosci(T))