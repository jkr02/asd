import collections


def DFS(G):
    time=0
    n=len(G)
    visited=[None]*n
    parent=[None]*n
    def DFSVisit(G, u):
        nonlocal time, visited, parent
        time+=1
        visited[u]=True
        for v in G[u]:
            if not visited[v]:
                parent[v]=u
                DFSVisit(G, v)
        time+=1
    for u in range(n):
        if not visited[u]:
            DFSVisit(G, u)
    print(parent)
def BFS(G, s):
    q=collections.deque()
    n=len(G)
    distance=[0]*n
    parents=[None]*n
    visited=[None]*n
    q.append(s)
    while q:
        u=q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v]=True
                distance[v]=distance[u]+1
                parents[v]=u
                q.append(v)
graph=[[1, 2],[2],[0, 3],[3]]
DFS(graph)