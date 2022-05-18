import collections

from zad7testy import runtests

def droga( G ):
    n=len(G)
    P=collections.deque()
    visited=[False for _ in range(n)]
    parents=[-1 for _ in range(n)]
    tab = []
    def spojny(G):
        nonlocal n
        class w:
            def __init__(self):
                self.visit=False
        t=[w() for _ in range(n)]
        P=collections.deque()
        P.append(0)
        while P:
            u=P.popleft()
            for v in G[u][0]:
                if not t[v].visit:
                    t[v].visit=True
                    P.append(v)
            for v in G[u][1]:
                if not t[v].visit:
                    t[v].visit=True
                    P.append(v)
        for i in range(n):
            if not t[i].visit:
                return False
        return True
    def lisc(G):
        nonlocal n
        for i in range(n):
            if len(G[i][0])==0 or len(G[i][1])==0:
                return True
        return False

    def dfs(s, d):
        nonlocal tab, G, visited,w, p, n, parents
        visited[s]=True
        if d==n:
            if parents[s] not in G[s][0]:
                if p in G[s][0]:
                    if w==1 and s in G[p][0]:
                        tab.append(s)
                        return True
                    if w==0 and s in G[p][1]:
                        tab.append(s)
                        return True
            if parents[s] not in G[s][1]:
                if p in G[s][1]:
                    if w == 1 and s in G[p][0]:
                        tab.append(s)
                        return True
                    if w == 0 and s in G[p][1]:
                        tab.append(s)
                        return True
            visited[s]=False
            return False
        if parents[s] not in G[s][0]:
            for i in range(len(G[s][0])):
                if not visited[G[s][0][i]]:
                    parents[G[s][0][i]]=s
                    if dfs(G[s][0][i], d+1):
                        tab.append(s)
                        return True
        if parents[s] not in G[s][1]:
            if s==p:
                w=1
            for i in range(len(G[s][1])):
                if not visited[G[s][1][i]]:
                    parents[G[s][1][i]] = s
                    if dfs(G[s][1][i], d+1):
                        tab.append(s)
                        return True
        visited[s]=False
        return False
    if not spojny(G):
        return None
    if lisc(G):
        return None
    for i in range(n):
        w=0
        p=i
        for j in range(n):
            visited[j]=False
            parents[j]=-1
        if dfs(p, 1):
            return tab[::-1]
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( droga, all_tests = True )