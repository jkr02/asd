import queue


class Node:
    def __init__( self, val ):
        self.next = None
        self.val = val

def function(L, s, t):
    n=len(L)
    def relax(dystans, a, b, val):
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
    while q:
        d, u = q.get()
        if visited[u]:
            continue
        visited[u]=True
        for v, w in L[u]:
            if not v in parents[u]:
                relax(distance, u, v, w)
                q.put((distance[v], v))
    return parents


L =  [[0,1,2,4,5],[0,10,20],[5,15,25]]
print(function(L,0, 7))