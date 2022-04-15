from random import randint

X = [randint(0, 10) for _ in range(10)]
Y = [randint(0, 10) for _ in range(10)]
print(X)
print(Y)

def NWP(A, B):
    m=len(A)
    n=len(B)
    tab=[[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if A[j]==B[i]:
                tab[i][j]=tab[i-1][j-1]+1
            else:
                tab[i][j]=max(tab[i-1][j], tab[i][j-1])
    return tab[n-1][m-1]
print(NWP(X, Y))