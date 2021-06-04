#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main()
{
    int a, p, d, x, y, x1, x2, q, r;
    do
    {
        printf("Nhap p= ");
        scanf("%d",&p);
        printf("Nhap a= ");
        scanf("%d",&a);
    }while (a < 1 || a >= (p - 1));
    int u = a, v = p;
    x2 = 0, x1 = 1;
    while (u != 1)
    {
        q = v / u;
        r = v % u;
        x = x2 - q * x1;
        v = u;
        u = r;
        x2 = x1;
        x1 = x;
    }
    printf("%d^-1 mod %d = %d",a,p, x1);
}
