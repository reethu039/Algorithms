#include <stdio.h>
#include <stdbool.h>
#define MAX 10
#define INF 9999

void dijkstra(int Graph[MAX][MAX], int n, int start) {
    int cost[MAX][MAX], distance[MAX], pred[MAX];
    bool visited[MAX];
    int i, j;

    // Creating cost matrix
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            cost[i][j] = Graph[i][j];

    for (i = 0; i < n; i++) {
        distance[i] = cost[start][i];
        pred[i] = start;
        visited[i] = false;
    }

    distance[start] = 0;
    visited[start] = true;

    for (int count = 0; count < n - 1; count++) {
        int min_distance = INF;
        int next_node = 0;

        for (i = 0; i < n; i++)
            if (distance[i] < min_distance && !visited[i]) {
                min_distance = distance[i];
                next_node = i;
            }

        visited[next_node] = true;
        for (i = 0; i < n; i++)
            if (!visited[i])
                if (min_distance + cost[next_node][i] < distance[i]) {
                    distance[i] = min_distance + cost[next_node][i];
                    pred[i] = next_node;
                }
    }
    
    // Printing the shortest paths
    for (i = 0; i < n; i++)
        if (i != start)
            printf("%d %d %d\n", start + 1, i + 1, distance[i]);
}
    
int main() {
    int Graph[MAX][MAX], vertices, edges, start_node = 0, u, v, w;
    scanf("%d",&vertices);
    scanf("%d",&edges);
    
    // Initialize adjacency matrix with INF
    for (int i = 0; i < MAX; i++) {
        for (int j = 0; j < MAX; j++) {
            Graph[i][j] = INF;
        }
    }
    
    // Input weights into adjacency matrix
    for (int i = 0; i < edges; i++) {
        scanf("%d %d %d", &u, &v, &w);
        Graph[u - 1][v - 1] = w;
    }

    dijkstra(Graph, vertices, start_node);

    return 0;
}
