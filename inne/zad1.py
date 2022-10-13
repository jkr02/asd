import queue
def function(L, s, t):
    n=len(L)
    def relax(dystans, parents, a, b, val):
        if dystans[b]>dystans[a]+val:
            parents[b].clear()
            parents[b].append(a)
            dystans[b]=dystans[a]+w
        elif dystans[b]==dystans[a]+w:
            parents[b].append(a)
    distance = [float("inf")]*n
    distance[s]=0
    parents=[[] for _ in range(n)]
    visited=[False]*n
    q=queue.PriorityQueue()
    q.put((0, s))
    while not q.empty():
        d, u = q.get()
        if visited[u]:
            continue
        visited[u]=True
        for v, w in L[u]:
            if not v in parents[u]:
                relax(distance, parents, u, v, w)
                q.put((distance[v], v))
    result=[]
    def Wyszukaj(u):
        while len(parents[u])>0:
            v=parents[u][0]
            Wyszukaj(v)
            parents[u].remove(v)
            result.append((v, u))
    Wyszukaj(t)
    return result
T=[[(1,2),(2,4)],
   [(0,2),(3,11),(4,3)],
   [(0,4),(3,13)],
   [(1,11),(2,13),(5,17),(6,1)],
   [(1,3),(5,5)],
   [(3,17),(4,5),(7,7)],
   [(3,1),(7,3)],
   [(5,7),(6,3)]]
print(function(T, 0, 7))