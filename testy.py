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
# print(suma)
print(float('inf')==float('inf')+1)
