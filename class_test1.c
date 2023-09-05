#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int uniqueElements(int arrSize, int arr[]){
    for(int i=0; i<arrSize; i++) {
        for (int j=i+1; j<arrSize; j++) {
            if(arr[i] == arr[j]) {
                return -1;
            }
        }
    }
    return 1;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    int arrSize;
    scanf("%d",&arrSize);
    if(arrSize==0) {
        printf("0");
        return 0;
    }
    int arr[arrSize];
    for(int i=0; i<arrSize; i++) {
        scanf("%d",&arr[i]);
    }
    int result = uniqueElements(arrSize, arr);
    printf("%d",result);
    return 0;
}