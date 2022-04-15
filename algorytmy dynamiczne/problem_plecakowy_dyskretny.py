W=[1, 3, 4, 5, 3, 4, 2]
C=[3, 4, 2, 6, 7, 9, 4]
w=10

def Knapsack(W, C, w):
    n=len(W)
    tab=[[0 for _ in range(w+1)] for _ in range(n)]
    for i in range(n):
        for j in range(w+1):
            if j>=W[i]:
                tab[i][j]=max(tab[i-1][j], C[i] + tab[i-1][j-W[i]])
            else:
                tab[i][j]=tab[i-1][j]
    return tab[n-1][w]
print(Knapsack(W, C, w))