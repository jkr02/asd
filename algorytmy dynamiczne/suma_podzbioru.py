A = [1,5,3,5,4,12]
T = 11

def SP(A, T):
    n = len(A)
    if sum(A)<T or min(A)>T:
        return False
    tab = [[0 for _ in range(T+1)] for _ in range(n)]
    for i in range(n):
        tab[i][0]=1
    for i in range(n):
        for j in range(T+1):
            tab[i][j]=tab[i-1][j]
            if j-A[i]>=0:
                tab[i][j]+=tab[i-1][j-A[i]]
    if tab[n-1][T]>0:
        return True
    return False

print(SP(A, T))


