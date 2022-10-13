#zlozonosc V^2
def tasks(T):
    def DFSVisit(graph, u):
        visited[u]=True
        for v in range(n):
            if graph[u][v]==2 and not visited[v]:
                DFSVisit(graph, v)
        result.append(u)
    n=len(T)
    result=[]
    visited=[False]*n
    for u in range(n):
        if not visited[u]:
            DFSVisit(tab, u)
    return result

tab=[[0,2,1,1],[1,0,1,1],[2,2,0,1],[2,2,2,0]]
print(tasks(tab))