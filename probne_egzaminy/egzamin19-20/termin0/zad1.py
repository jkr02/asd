from queue import PriorityQueue

def islands(G, A, B):
    def dijkstra_matrix(graph, start):
        distances = [float("inf") for _ in range(len(graph))]
        visited = [False for _ in range(len(graph))]
        distances[start] = 0
        while True:
            shortest_distance = float("inf")
            shortest_index = -1
            for i in range(len(graph)):
                if distances[i] < shortest_distance and not visited[i]:
                    shortest_distance = distances[i]
                    shortest_index = i
            if shortest_index == -1:
                return distances
            for i in range(len(graph[shortest_index])):
                if graph[shortest_index][i] != 0 and distances[i] > distances[shortest_index] + graph[shortest_index][i]:
                    distances[i] = distances[shortest_index] + graph[shortest_index][i]
            visited[shortest_index] = True
    dystans = dijkstra_matrix(G, A)
    return dystans[B]
graf= [ [0,5,1,8,0,0,0 ],
[5,0,0,1,0,8,0 ],
[1,0,0,8,0,0,8 ],
[8,1,8,0,5,0,1 ],
[0,0,0,5,0,1,0 ],
[0,8,0,0,1,0,5 ],
[0,0,8,1,0,5,0 ] ]
print(islands(graf, 5, 2))