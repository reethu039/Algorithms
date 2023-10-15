#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    char val1, val2;
    int vertices=0;
    
    scanf("%d",&vertices);
    if(vertices==0){
        printf("0");
        return 0;
    } 
    else if (vertices==1){
        scanf("%c",&val1);
        printf("%c",val1);
        return 0;
    }
    
    int matrix[10][10];
    int adj[10];
    
    for(int i=0; i<vertices; i++){
        for(int j=0; j<vertices; j++) {
            matrix[i][j]=0;
        }
    }
    
    int num=0;
    while(num<vertices)
    {
        scanf(" %c %c",&val1,&val2);
        matrix[val1-'A'][val2-'A']=1;
        num++;
    }
    
    for(int i=0; i<vertices; i++){
        num=0;
        for(int j=0; j<vertices; j++) {
            if(matrix[j][i]==1){
                num++;
            }
        }
        adj[i]=num;
    }
    
    for(int i=0; i<vertices; i++){
        printf("%d ",adj[i]);
    }
}