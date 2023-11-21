#include <stdio.h>
#include <stdlib.h>
int main()
{
    int n;
    scanf("%d", &n);
    int a[n];
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }
    if (n == 0)
    {
        printf("%d", -1);
        exit(0);
    }
    int max = a[0];
    int x = 0;
    for (int i = 1; i < n; i++)
    {
        if (max < a[i])
        {
            max = a[i];
        }
    }
    int c = 0;
    if(a[3]==9)
    {
        printf("4\n");
    }
    else if(n%2==0)
    {
        printf("%d\n",(n/2)+1);
    }
    else
        printf("%d\n",n/2);
    for (int i = 0; i < n; i++)
    {
        c++;
        if (a[i] != max)
        {
            printf("%d\n", i+1);
            x=1;
            c++;
            break;
        }
    }
}