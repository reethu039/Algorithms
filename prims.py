def prims(graph, vertices):
    selected = [False] * vertices
    selected[0] = True
    edge_count = min_cost = 0
    
    while edge_count < vertices-1:
        min = INF
        s = 0
        for i in range(vertices):
            if selected[i]==True:
                for j in range(vertices):
                    if selected[j]==False and graph[i][j]<min:
                        min = graph[i][j]
                        s = j
        min_cost += min
        selected[s] = True
        edge_count += 1
    
    print(min_cost)
    

vertices = int(input(""))
edges = int(input(""))
INF = 9999
graph = [([INF] * vertices) for i in range(vertices)]

for i in range(edges):
    u, v, weight = map(int, input("").split())
    graph[u-1][v-1] = weight

prims(graph, vertices)