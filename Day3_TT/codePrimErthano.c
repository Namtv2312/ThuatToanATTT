#include <stdio.h>
#include <stdlib.h>
 
#define limit 100 /*size of integers array*/
 
int main(){
    unsigned long long int i,j;
    int *primes;
    int z = 1;
 
    primes = malloc(sizeof(int) * limit);
 
    for (i = 2;i < limit; i++)
        primes[i] = 1;
 
    for (i = 2;i < limit; i++)
        if (primes[i])
            for (j = i;i * j < limit; j++)
                primes[i * j] = 0;
 
    printf("\nSo nguyen to tu 1 den n la: \n");
    for (i = 2;i < limit; i++)
        if (primes[i])
            printf("%d\n", i);
 
return 0;
}