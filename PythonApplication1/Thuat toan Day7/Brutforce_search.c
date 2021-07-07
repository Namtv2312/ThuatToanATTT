#include<stdio.h>
#include<string.h>
void BruteForce(char T[], char P[]) {
    int check = 0;
    int loop = 0;
    int operato = 0;
    int n = strlen(T);
    int m = strlen(P);
    for (int i = 0; i <= n - m; i++) {
        int j = 0;
        while (j < m && T[i + j] == P[j]) {
            operato++;
            j++;
        }
        if (j == m) {
            check = 1;
            printf("Thay o vi tri %d\n", i);
            printf("So phep toan %d\n", operato);
            printf("So vong lăp %d\n", loop);
        }
        else {
            loop++;
            operato++;
        }
    }
    if (check != 1) {
        printf("\nKhong tim thay");
        printf("\nSo phep toan %d", operato);
        printf("\nSo vong lap %d", loop);
    }
}
int main()
{
    char T[] = "aaaaaaaaaaaaaaaaaaaaaaaaaah";
    char P[] = "aaah";
    BruteForce(T, P);
    return 0;
}
