def floyd_warshall(graph, vertices):

    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for i in range(vertices):
        for j in range(vertices):
            if i != j:
                print(f"{i + 1} {j + 1} {graph[i][j]}")


vertices = int(input(""))
edges = int(input(""))

if edges != 0:
    graph = [([9999] * vertices) for i in range(vertices)]
    
    for i in range(edges):
        source, dest, weight = map(int, input().split())
        graph[source - 1][dest - 1] = weight
    floyd_warshall(graph, vertices)
    
else:
    print(-1)