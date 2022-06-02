def T_closure(M):
    TM=M.copy()
    n=len(M)
    for k in range(n):
        for v in range(k):
            for u in range(k):
                TM[u][v] = TM[u][v] or (TM[u][k] and TM[k][v])