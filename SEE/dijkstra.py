def dijkstra(Graph, vertices):
    start = 0
    distance = [Graph[start][i] for i in range(vertices)]
    pred = [start] * vertices
    visited = [False] * vertices

    distance[start] = 0
    visited[start] = True

    for count in range(vertices - 1):
        min_distance = INF
        next_node = 0

        for i in range(vertices):
            if distance[i] < min_distance and not visited[i]:
                min_distance = distance[i]
                next_node = i

        visited[next_node] = True
        for i in range(vertices):
            if not visited[i]:
                if min_distance + Graph[next_node][i] < distance[i]:
                    distance[i] = min_distance + Graph[next_node][i]
                    pred[i] = next_node

    # Printing the shortest paths
    for i in range(vertices):
        if i != start:
            print(start + 1, i + 1, distance[i])

MAX = 10
INF = 9999
Graph = [([INF] * MAX) for i in range(MAX)]

vertices = int(input())
edges = int(input())

for i in range(edges):
    u, v, w = map(int, input().split())
    Graph[u - 1][v - 1] = w

dijkstra(Graph, vertices)