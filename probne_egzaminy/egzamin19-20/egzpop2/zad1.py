import collections


def best_root(L):
    n=len(L)
    stopnie = [len(L[i]) for i in range(n)]
    max_path=[1 for _ in range(n)]
    q=collections.deque()
    for i in range(n):
        if stopnie[i]==1:
            q.append(i)
    while len(q)>=2:
        u=q.popleft()
        v = L[u][0]
        if max_path[u]+1>max_path[v]:
            max_path[v]+=1
        L[u].remove(v)
        L[v].remove(u)
        stopnie[u]-=1
        stopnie[v]-=1
        if len(L[v])==1:
            q.append(v)
    ind=0
    maks=-1
    for i in range(n):
        if maks<max_path[i]:
            maks=max_path[i]
            ind=i
    return ind

L = [ [ 2 ],[ 2 ],[ 0, 1, 3],[ 2, 4 ],[ 3, 5, 6 ],[ 4 ],[ 4 ] ]
print(best_root(L))
