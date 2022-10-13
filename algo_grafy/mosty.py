import queue


def find_bridges(G):
    n = len(G)
    visited = [False] * n
    processed = [False] * n
    d = [float("inf")] * n
    low = [float("inf")] * n
    parents = [None] * n
    time = 1
    result = []
    def dfs_visit(v):
        visited[v] = True
        nonlocal time
        d[v] = time
        low[v] = time
        time += 1
        min_back = float("inf")
        for u in G[v]:
            if not visited[u]:
                parents[u] = v
                dfs_visit(u)
            if (visited[u] and not processed[u] and u != v and parents[v] != u):
                min_back = min(min_back, low[u])
        low[v] = min(low[v], min_back)
        for u in G[v]:
            if parents[u] == v:
                low[v] = min(low[v], low[u])
        if low[v] == d[v]:
            result.append((v, parents[v]))
        processed[v] = True
    dfs_visit(0)
    result.pop(result.index((0, None)))
    return result


def most(T):
    n=len(T)
    def DFSVisit(t, s):
        nonlocal time
        time+=1
        visited[s]=True
        d[s]=time
        for v in T[s]:
            if not visited[v]:
                parent[v]=s
                DFSVisit(t, v)
        time+=1
        proceed[s]=time
    d=[float("inf") for _ in range(n)]
    visited=[False]*n
    parent=[None]*n
    proceed=[float("inf")]*n
    time=0
    low=[float("inf")]*n
    for i in range(n):
        if not visited[i]:
            DFSVisit(T,i)
    q=queue.PriorityQueue()
    for i in range(n):
        q.put((proceed[i], i))
    while not q.empty():
        c, v=q.get()
        lowest=float("inf")
        d_low=float("inf")
        for u in T[v]:
            if parent[u]==v and low[u]<d_low:
                d_low=low[u]
            if d[u]<lowest and parent[v]!=u:
                lowest=d[u]
        low[v]=min(d[v], lowest, d_low)
    tmp=[]
    for i in range(n):
        if low[i]==d[i]:
            tmp.append((parent[i], i))
    result=[]
    for i in tmp:
        if i[0]==None:
            continue
        result.append(i)
    return result
tab=[[1, 6],
     [0, 2],
     [1, 6, 3],
     [2, 4, 5],
     [3, 5],
     [3, 4],
     [0, 2, 7],
     [6]]
print(most(tab))
