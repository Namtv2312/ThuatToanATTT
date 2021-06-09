#include <stdio.h>
#include <math.h>
int main()
{ int n;  int a[100],b[100],j=0;
    for(int i=0;i<100;i++)
    {
        a[i]=b[i]=0;
    }
     
    printf("Nhap n: ");
    scanf("%d",&n);
    int dem ;
    for (int i=2;i<=n;i++)
    {
        dem=0;
        while(n%i==0)
        {
            ++dem;
            n/=i;
        }
        if(dem>=1)
        {
            a[j]=i;
            b[j]=dem;
            j++;
        }
        
    }
    printf("Coso=[");
    for(int i=0;i<j;i++)
    {
            printf("%d ",a[i]);
    }
    printf("] Somu=[");
    for(int i=0;i<j;i++)
    {
            printf("%d ",b[i]);
    }
    printf("]");
}