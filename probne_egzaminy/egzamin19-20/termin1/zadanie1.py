def zbigniew(A):
    n=len(A)
    o=A[0]
    visited=[False for _ in range(n)]
    visited[0]=True
    r=1
    while True:
        maksimum=0
        for i in range(1, r+1):
            if visited[i]==False and maksimum<A[i]:
                maksimum=A[i]
                ind=i
        if maksimum==0:
            return None
        o+=maksimum
        r+=1
        visited[ind]=True
        if o>=n-1:
            return r