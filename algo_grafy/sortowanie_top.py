def Sort_top(G, n):
    """lista sasiedztwa"""
    visited=[None]*n
    stack=[]
    def SortVisit(G, u):
        nonlocal visited, stack
        visited[u]=True
        for v in G[u]:
            if not visited[v]:
                SortVisit(G, v)
        stack.insert(0, u)
    for u in range(n):
        if not visited[u]:
            SortVisit(G, u)
    print(stack)

