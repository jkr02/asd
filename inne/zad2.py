def order(L, K):
    A=[[] for _ in range(10**K)]
    B=[[] for _ in range(10**K)]
    for x in L:
        A[x%(10**K)].append(x)
        B[x//(10**K)].append(x)
    print(A)
    print(B)
    d_s=[len(A[i])-len(B[i]) for i in range(10 ** K)]
    no=[0,0,0]
    for i in range(10**K):
        if abs(d_s[i])>1: return None
        no[d_s[i]]+=1
    if no[1]>1 or no[-1]>1: return None

L=[56, 15, 31, 43, 54, 35, 12, 23]
K=1
order(L, K)