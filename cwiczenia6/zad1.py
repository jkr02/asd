#funkcja sprawdza czy da sie wybrac podciag z tablicy A, które sumuja sie do zadanej wartosci T
from random import randint
A=[randint(1, 14923) for _ in range(10)]
T = 1748323
def rekursive(i, suma):
    global A
    for x in range(i, len(A)):
        suma += A[x]
        if suma == T:
            return True
        if rekursive(x+1, suma):
            return True
        suma -= A[x]
    return False
#print(rekursive(0, 0))
def subset(A, T):
    """niby dynamiczny, ale dla duzego T i malej ilosci danych to jednak nie taki dynamiczny"""
    n=len(A)
    F=[[0 for _ in range(T+1)]for x in range(n)]
    for i in range(n):
        F[i][0]=1
    for i in range(n):
        for j in range(T+1):
            F[i][j]=F[i-1][j]
            if j-A[i]>=0:
                F[i][j]=F[i-1][j-A[i]]
    return F[n-1][T]
print(subset(A, T))