#include <stdio.h>
#include <math.h>

long int n;

void nhap()
{
    printf("nhap n = ");
    scanf("%ld", &n);
}

long int tim_ucln(long int a,long int b)
{
    long int r;
    if (a < b)
    {
        r = a;
        a = b;
        b = r;
    }
    while (b > 0)
    {
        r = a % b;
        a = b;
        b = r;
    }
    return a;
}

void thua_so_khong_tam_thuong()
{
    long int a = 2, b = 2, i = 1;
    long int d, bp_a, bp_b;
    while (1)
    {
        a=(a*a+1)%n;
        b=(b*b+1)%n;
        b=(b*b+1)%n;
        d = tim_ucln(a - b, n);
        if (d > 1 && d < n)
        {
            printf("d = %ld", d);
            break;
        }
        else if (d == n)
        {
            // that bai thay doi c != 0, != -2
            i++;
        }
    }
}

int main()
{
    nhap();
    thua_so_khong_tam_thuong();
    return 0;
}