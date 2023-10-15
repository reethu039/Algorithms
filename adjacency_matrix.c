#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int adj[10];
    int num=0, vertices=0, val1, val2;
    int matrix[10][10];
    
    scanf("%d",&vertices);
    if(vertices==0){
        printf("-1");
        return 0;
    } 
    else if (vertices==1){
        scanf("%d",&val1);
        printf("%d",val1);
        return 0;
    }
    
    while(1){
        if((scanf("%d%d",&val1,&val2))!=2){
            break;
        }
        matrix[val1-1][val2-1]=1;
    }
    
    for(int i=0; i<vertices; i++){
        if(matrix[val1-1][i]==1){
            adj[num]=i+1;
            num++;
        }
    }
    
    printf("%d\n",num);
    for(int i=0; i<num-1; i++){
        printf("%d,",adj[i]);
    }
    printf("%d",adj[num-1]);
    
}