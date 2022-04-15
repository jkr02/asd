C = [1, 4, 5, 2, 8, 10]
W = [1, 3, 4, 2, 6, 7]
w=15

def Knapsack(W, C, w):
    n=len(W)
    tab = [0 for _ in range(n)]
    for i in range(n):
        tab[i] = C[i]/W[i]
    for i in range(n):
        for j in range(n):
            return