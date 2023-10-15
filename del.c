#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int vertices;
    scanf("%d",&vertices);
    if(vertices==0)
    {
        printf("0");
        return 0;
    }
    if(vertices==1)
    {
        int temp;
        scanf("%d",&temp);
        printf("%d",temp);
        return 0;
    }
    
    int A[10][10];
    int adj[10];
    for(int i=0;i<vertices;i++)
    {
        for (int j=0;j<vertices;j++)
        {
            A[i][j]=0;
        }
    }
    char temp1,temp2;
    int k=0;
    while(k<vertices)
    {
        scanf(" %c %c",&temp1,&temp2);
        A[(temp1-'A' + 1)-1][(temp2-'A' + 1)-1]=1;
        k++;
    }
    
    for(int i=0;i<vertices;i++)
    {   int num=0;
        for(int j=0;j<vertices;j++)
        {
            if(A[j][i]==1)
            {
                num++;
            }
        }
       adj[i]=num;
    }
    
    for(int i=0;i<vertices;i++)
    {
        printf("%d ",adj[i]);
    }
    return 0;
}
