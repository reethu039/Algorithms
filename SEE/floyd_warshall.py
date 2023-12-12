def floyd_warshall(graph, vertices):
    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
    
    for i in range(vertices):
        for j in range(vertices):
            if i!=j:
                print(i+1, j+1, graph[i][j])

vertices = int(input(""))
edges = int(input(""))
INF = 9999

if edges!=0:
    graph = [([INF] * vertices) for i in range(vertices)]
    for i in range(edges):
        u, v, weight = map(int, input("").split())
        graph[u-1][v-1] = weight
    floyd_warshall(graph, vertices)
    
else:
    print("-1")