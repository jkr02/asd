import collections

from zad7testy import runtests
def droga( G ):
    n=len(G)
    visited=[False for _ in range(n)]
    parents=[-1 for _ in range(n)]
    tab = []
    def dfs(s, d):
        nonlocal tab, G, visited,w, p, n, parents
        visited[s]=True
        if d==n:
            if parents[s] in G[s][0]:
                if p in G[s][1]:
                    if w==1 and s in G[p][0]:
                        tab.append(s)
                        return True
                    if w==0 and s in G[p][1]:
                        tab.append(s)
                        return True
            if parents[s] in G[s][1]:
                if p in G[s][0]:
                    if w == 1 and s in G[p][0]:
                        tab.append(s)
                        return True
                    if w == 0 and s in G[p][1]:
                        tab.append(s)
                        return True
            visited[s]=False
            return False
        if parents[s] in G[s][1]:
            for i in range(len(G[s][0])):
                if not visited[G[s][0][i]]:
                    parents[G[s][0][i]]=s
                    if dfs(G[s][0][i], d+1):
                        tab.append(s)
                        return True
        if parents[s] in G[s][0]:
            for i in range(len(G[s][1])):
                if not visited[G[s][1][i]]:
                    parents[G[s][1][i]] = s
                    if dfs(G[s][1][i], d+1):
                        tab.append(s)
                        return True
        visited[s]=False
        return False
    for i in range(n):
        print(i)
        p=i
        visited[p]=True
        w=0
        for j in range(n):
            visited[j]=False
            parents[j]=-1
        for j in range(len(G[p][0])):
            print(G[p][0][j])
            parents[G[p][0][j]]=p
            if dfs(G[p][0][j], 2):
                tab.append(p)
                return tab[::-1]
        w=1
        for j in range(len(G[p][1])):
            print(G[p][1][j])
            parents[G[p][1][j]]=p
            if dfs(G[p][1][j], 2):
                tab.append(p)
                return tab[::-1]
        visited[p]=False
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( droga, all_tests = True )