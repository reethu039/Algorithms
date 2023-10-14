#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

typedef struct node {
    int val;
    struct node* next;
} n;

typedef struct list {
    struct node* head;
} l;

l* create_list(int i);
void add_list(l* list, int i);
void traverse(l* list);

int main() {
    int vertices = 0;
    scanf("%d", &vertices);
    if(vertices == 0)
    {
        printf("-1");
        exit(0);
    }
    if(vertices == 1)
    {
        int temp;
        scanf("%d",&temp);
        printf("%d",temp);
        exit(0);
    }
    
    l list[vertices];
    
    for (int i = 0; i < vertices; i++) {
        list[i] = *create_list(i + 1);
    }

    int temp1, temp2;
    
    while (1) {
        if (scanf("%d %d", &temp1, &temp2) != 2) {
            break;  
        }
        add_list(&list[temp1 - 1], temp2);
    }
    
    traverse(&list[temp1 - 1]);

    return 0;
}

l* create_list(int i) {
    l* li;
    n* node;
    li = (l*)malloc(sizeof(l));
    node = (n*)malloc(sizeof(n));
    li->head = node;
    node->val = i;
    node->next = NULL;
    return li;
}

void add_list(l* list, int i) {
    n* node;
    n* curr;
    node = (n*)malloc(sizeof(n));
    node->val = i;
    node->next = NULL;
    curr = list->head;
    while (curr->next != NULL) {
        curr = curr->next;
    }
    curr->next = node;
}

void traverse(l* list) {
    n* curr = list->head->next;  
    int num = 0;
    
    while (curr != NULL) {
        num++;
        curr = curr->next;
    }
    
    printf("%d\n", num);
    
    curr = list->head->next;  
    while (curr != NULL) {
        if (curr->next == NULL) {
            printf("%d\n", curr->val);
        } else {
            printf("%d,", curr->val);
        }
        curr = curr->next;
    }
}