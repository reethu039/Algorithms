#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

#define max 1000

typedef struct queue
{
    int ver;
    int dist;
} queue;

typedef struct node 
{
    int ver;
    struct node* next;
} node;


typedef struct list
{
    node* head;
} list;

typedef struct graph 
{
    list adjacency_list[max];
} graph;

void init_graph(graph* g, int num_ver) 
{
    for (int i = 0; i < num_ver; ++i) 
        g->adjacency_list[i].head = NULL;
}

void add_edge(graph* g, int start, int end) 
{
    node* new_node = (node*)malloc(sizeof(node));
    new_node->ver = end;
    new_node->next = g->adjacency_list[start].head;
    g->adjacency_list[start].head = new_node;
    new_node = (node*)malloc(sizeof(node));
    new_node->ver = start;
    new_node->next = g->adjacency_list[end].head;
    g->adjacency_list[end].head = new_node;
}

int shortest_path(graph* g, int num_ver, int start, int end) 
{
    bool visited[max];
    memset(visited, false, sizeof(visited));
    queue q[max];
    int front = 0, rear = 0;
    q[rear].ver = start;
    q[rear].dist = 0;
    rear++;
    visited[start] = true;
    while (front < rear) 
    {
        queue current = q[front];
        front++;
        if (current.ver == end) 
            return current.dist;
        node* temp = g->adjacency_list[current.ver].head;
        while (temp) 
        {
            if (!visited[temp->ver]) 
            {
                q[rear].ver = temp->ver;
                q[rear].dist = current.dist + 1;
                rear++;
                visited[temp->ver] = true;
            }
            temp = temp->next;
        }
    }
    return -1;
}

int main() 
{
    int num_ver, num_edges;
    scanf("%d%d", &num_ver, &num_edges);
    if (num_edges == 0) 
    {
        printf("-1\n");
        return 0;
    }
    graph g;
    init_graph(&g, num_ver);
    for (int i = 0; i < num_edges; ++i) 
    {
        int start, end;
        scanf("%d,%d", &start, &end);
        add_edge(&g, start, end);
    }
    int start, end;
    scanf("%d,%d", &start, &end);
    int min_edges = shortest_path(&g, num_ver, start, end);
    printf("%d\n", min_edges);
}