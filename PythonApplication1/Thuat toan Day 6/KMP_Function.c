//thuat toan KMP_algorithm
#include <stdio.h>
#include <string.h>
void remove_spaces(char* s) {
    const char* d = s;
    do {
        while (*d == ' ') {
            ++d;
        }
    } while (*s++ = *d++);
}
int* Failture_FC(char P[])
{
    remove_spaces(P);
    int F[strlen(P)];
    int* p = F;
    F[0] = -1;
    int i = 2;
    int j = 0;
    for (int i = 2; i < strlen(P); i++) {
        if (P[i - 1] == P[j]) {
            F[i] = j + 1;
            i++;
            j++;
        }
        else if (j > 0) {
            j = F[j];
        }
        else {
            F[i] = 0;
            i++;
        }
    }
    return p;
}
void KMP_algorithm(char T[], char P[])
{
    int* F = Failture_FC(P);
    for (int i = 0; i < strlen(P); i++) {
        printf("%d\n", *(F + i));
    }
    int k = 0;
    int check = 0;
    int i, j;
    i = 0;
    j = 0;
    int count = 0;
    int operato = 0;
    int loop = 0;
    while (i < strlen(T))
    {
        if (T[k] == P[j]) {
            operato++;
            count++;
            k++;
            j++;
        }
        else {
            operato++;
            loop++;
            count = 0;
            i = i + j - F[j];
            j = (F[j] != 0) ? F[j] : 0;
            k = i;
        }
        if (count == strlen(P)) {
            check = 1;
            printf("Thay o vi tri %d\n", i);
            printf("So phep toan %d\n", operato);
            printf("So vong lăp %d\n", loop);
        }
    }

    if (check != 1)
    {
        printf("\nKhong tim thay");
        printf("\nSo phep toan %d", operato);
        printf("\nSo vong lap %d", loop);
    }
}
int main()
{
    char T[] = "abacaabacabaabb";
    char P[] = "abacab";
    KMP_algorithm(T, P);
    return 0;
}
