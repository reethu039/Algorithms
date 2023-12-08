INF = 9999

def prims(G, vertices):
    selected = [False] * MAX

    selected[0] = True
    edge_count = 0
    min_cost = 0

    while edge_count < vertices - 1:
        min = INF
        y = 0

        for i in range(vertices):
            if selected[i]:
                for j in range(vertices):
                    if not selected[j] and G[i][j] < min:
                        min = G[i][j]
                        y = j

        min_cost += min
        selected[y] = True
        edge_count += 1

    print(min_cost)


MAX = 100
G = [[INF] * MAX for i in range(MAX)]

vertices = int(input(""))
edges = int(input(""))

for i in range(edges):
    u, v, w = map(int, input().split())
    G[u - 1][v - 1] = w

prims(G, vertices)