#include<stdio.h>
#include<stdbool.h>

#define MAX 100
#define INF 9999

void prims(int G[MAX][MAX], int vertices){
    bool selected[MAX];

    // Set selected vertices to false initially
    for (int i = 0; i < MAX; i++) {
        selected[i] = false;
    }

    selected[0] = true;
    int edgeCount = 0;
    int min_cost = 0;

    while (edgeCount < vertices - 1) {
        int min = INF;
        int y = 0;

        for (int i = 0; i < vertices; i++) {
            if (selected[i]) {
                for (int j = 0; j < vertices; j++) {
                    if (!selected[j] && G[i][j] < min) {
                        min = G[i][j];
                        y = j;
                    }
                }
            }
        }
        min_cost += min;
        selected[y] = true;
        edgeCount++;
    }

    printf("%d\n", min_cost);
}

int main() {
    int vertices, edges, u, v, w;
    int G[MAX][MAX];
    
    
    scanf("%d", &vertices);
    scanf("%d", &edges);

    // Initialize adjacency matrix with INF
    for (int i = 0; i < MAX; i++) {
        for (int j = 0; j < MAX; j++) {
            G[i][j] = INF;
        }
    }
    
    // Input weights into adjacency matrix
    for (int i = 0; i < edges; i++) {
        scanf("%d %d %d", &u, &v, &w);
        G[u - 1][v - 1] = w;
    }

    prims(G, vertices);
    return 0;
}