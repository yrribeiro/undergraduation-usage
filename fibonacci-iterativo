#include <stdio.h>
#include <stdint.h>
#include <time.h>

void power(unsigned long long int M[][2], int n){
    int i;
    unsigned long long int upperLeft, upperRight, bottomLeft, bottomRight;
    unsigned long long int mAux[2][2] = {
        {1, 1},
        {1, 0}
    };
    for(i=2; i<=n; i++){
        upperLeft = M[0][0]*mAux[0][0] + M[0][1]*mAux[1][0];
        upperRight = M[0][0]*mAux[0][1] + M[0][1]*mAux[1][1];
        bottomLeft = M[1][0]*mAux[0][0] + M[1][1]*mAux[1][0];
        bottomRight = M[1][0]*mAux[0][1] + M[1][1]*mAux[1][1];

        M[0][0] = upperLeft;
        M[0][1] = upperRight;
        M[1][0] = bottomLeft;
        M[1][1] = bottomRight;
    }
}

unsigned long long int matrixFibonacci(int n){
    unsigned long long int M[2][2] = {
        {1, 1},
        {1, 0}
    };
    if (n==0){
        return 0;
    }
    power(M, n-1);
    return M[0][0];
}

int main(){
    time_t start, end;
    double executionTime;

    int n = 97;
    start = time(NULL);
    printf("%llu", matrixFibonacci(n));
    end = time(NULL);
    executionTime = (double)end-start;
    printf("\nExecution time: %.8lf\n", executionTime);
    return 0;
}
