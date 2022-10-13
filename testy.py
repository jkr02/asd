import collections
import time

print(float('inf'))
if 6<float('inf'):
    print("tso")
def BFS(a, b, tablica, parent, n):
    visited=[False for _ in range(n)]
    q=collections.deque()
    visited[a]=True
    q.append(a)
    while q:
        v=q.popleft()
        for u in range(n):
            if not visited[u] and tablica[v][u]>0:
                visited[u]=True
                q.append(u)
                parent[u]=v
    if visited[b]:
        return True
    return False
def edmonds_karp(tablica, a, b, n):
    parent = [-1 for _ in range(n)]
    maxflow=0
    while BFS(a, b, tablica, parent, n):
        pathflow=float("inf")
        z = a
        while z!=b:
            pathflow=min(pathflow, tablica[parent[z]][z])
            z = parent[z]
        maxflow+=pathflow
        z = a
        while z!=b:
            tablica[parent[z]][z]-=pathflow
            tablica[z][parent[z]]+=pathflow
            z=parent[z]
    return maxflow
#######################################################
# n = int(input("Podaj liczbę"))
# start=time.time()
# prev=[0 for _ in range(n+1)]
# print("1memory ok")
# next = [0 for _ in range(n+1)]
# print("2memory ok")
# for i in range(2, n+1):
#     prev[i]=i-1
#     next[i]=i+1
# next[n]=2
# prev[2]=n
# p=2
# while p**2<=n:
#     q=p
#     while q*p<=n:
#         r=p*q
#         while r<=n:
#             next[prev[r]]=next[r]
#             prev[next[r]]=prev[r]
#             next[r]=None
#             r=r*p
#         q=next[q]
#     p=next[p]
# stop=time.time()
# # for i in range(2, n+1):
# #     if next[i]:
# #         print(next[i], end=" ")
# print(stop-start)
suma = 0
# for x in range(1, 10000000):
#     suma+=(1/(2*x-1))
#     suma-=(1/(2*x))
# for x in range(1, 1000000):
# suma+=((-1)**(x+1))/((3*x-2)*(3*x+1))
# for x in range(1, 10000):
#     suma+=x/(2**x)
# for i in range(1, 10000000):
#     suma-=1/(2*i-1)
#     suma+=1/(2*i)
# # print(suma)
# print(float('inf')==float('inf')+1)
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
        stack.insert(0, v)
    def topologicalSort(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
        return stack
# g=Graph(4)
# g.addEdge(2, 0)
# g.addEdge(3, 0)
# g.addEdge(1, 2)
# g.addEdge(3, 2)
# g.addEdge(1, 3)
# g.topologicalSort()
def swaps(disk, depends):
    g=Graph(len(depends))
    for u in range(len(depends)):
        for v in range(len(depends[u])):
            g.addEdge(u, depends[u][v])
    stack = g.topologicalSort()
    i=-1
    zmian=0
    for j in range(1, len(depends)):
        i+=1
        if stack[i]%2==0 and stack[i]+1==stack[j]:
            continue
        zmian+=1
    return zmian
tab=[[2,3],[],[1, 3], [1]]
print(swaps(0, tab))
