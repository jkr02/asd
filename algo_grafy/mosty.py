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

            if (
                visited[u] and not processed[u] and u != v and parents[v] != u
            ):  # krawedz wsteczna
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
