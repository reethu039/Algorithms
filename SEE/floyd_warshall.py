def floyd_warshall(vertices, edges):
    graph = [[9999] * vertices for i in range(vertices)]
    
    for edge in edges:
        source, dest, weight = edge
        graph[source - 1][dest - 1] = weight

    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for i in range(vertices):
        for j in range(vertices):
            if i != j:
                print(f"{i + 1} {j + 1} {graph[i][j]}")


vertices = int(input(""))
edges_count = int(input(""))

if edges_count == 0:
    print(-1)
    exit(0)
edges = []
if edges_count==1:
    edge = int(input(""))
    edges.append(edge)
else:
    for i in range(edges_count):
        edge = list(map(int, input().split()))
        edges.append(edge)
    floyd_warshall(vertices, edges)