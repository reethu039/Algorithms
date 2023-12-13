def dijkstra(graph, vertices):
    start = 0
    distance = [graph[start][i] for i in range(vertices)]
    visited = [False] * vertices
    visited[start] = True
    
    for count in range(vertices-1):
        min_distance = INF
        next_node = 0
        
        for i in range(vertices):
            if distance[i] < min_distance and not visited[i]:
                min_distance = distance[i]
                next_node = i
        visited[next_node] = True
        
        for j in range(vertices):
            if not visited[j]:
                if min_distance + graph[next_node][j] < distance[j]:
                    distance[j] = min_distance + graph[next_node][j]
     
    for i in range(vertices):
        if i!=start:
            print(start+1, i+1, distance[i])
    

vertices = int(input(""))
edges = int(input(""))
INF = 9999

if vertices!=0 and edges!=0:
    graph = [([INF] * vertices) for i in range(vertices)]
    
    for i in range(vertices):
        graph[i][i] = 0
    
    for i in range(edges):
        u, v, weight = map(int, input("").split())
        graph[u-1][v-1] = weight
    
    dijkstra(graph, vertices)