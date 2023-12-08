def prims(graph, vertices):
    selected = [False] * vertices
    selected[0] = True
    edge_count = min_cost = 0
    
    while edge_count < vertices - 1:
        min = INF
        s = 0
        for i in range(vertices):
            if selected[i]==True:
                for j in range(vertices):
                    if (selected[j]==False) and (graph[i][j] < min):
                        min = graph[i][j]
                        s = j
        min_cost += min
        selected[s] = True
        edge_count += 1
        
    print(min_cost)
    

MAX = 100
INF = 9999
Graph = [([INF] * MAX) for i in range(MAX)]

vertices = int(input(""))
edges = int(input(""))

for i in range(edges):
    u, v, w = map(int, input("").split())
    Graph[u-1][v-1] = w

prims(Graph, vertices)