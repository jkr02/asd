def NM(p):
    n=len(p)
    m = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(1, n):
        m[i][i] = 0
    for L in range(2, n):
        for i in range(1, n - L + 1):
            j = i + L - 1
            m[i][j] = m[i][i] + m[i + 1][j] + p[i - 1] * p[i] * p[j]
            for k in range(i+1, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
    return m[1][n - 1]
arr = [1, 2, 3, 4]
print(NM(arr))