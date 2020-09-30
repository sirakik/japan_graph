#include<stdio.h>

int main(void){

    int n, a, bo, shi;
    scanf("%d", &n);
    scanf("%d", &a);
    shi = 1;
    bo = a;

    for(; n > 1; n--){
        scanf("%d", &a);
        int temp = bo;
        bo = shi;
        shi = temp;
        shi += bo * a;
    }
    printf("%d/%d (%f)\n", shi, bo, (double)shi/bo);

    return 0;
}