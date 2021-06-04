
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
int W, P, t, m,V;

int *
PAr (int a)// hàm trả về mảng từ số nguyên
{
  int A[t];
  int *p=A;
  for (int i = t - 1; i >= 0; i--)
    {
      A[i] = a / pow (2, i * W);
      a = a - A[i] * pow (2, i * W);
    }
  return p;
}
void  phep_tinhnhan(int A[], int B[])
{
    int C[100];int j;
    for(int i=0;i<=t-1;i++)
    {
        C[i]=0;
    }
        for(int i=0;i<t;i++)
        {
          int  U=0;int UV=0;
            for( j=0;j<t;j++)
            {
              UV=C[i+j]+A[i]*B[j]+U;
                
               U=UV/256;
               C[i+j]=UV%256;
                }
            C[i+t]=U;
        }
        for(int i=7;i>=0;i--)
        {
            printf("%d ",C[i]);
        }
    
}
int
main ()
{
    int a,b;
  printf ("Nhap so Wbit: ");
  scanf ("%d", &W);
  printf ("Nhap so p: ");
  scanf ("%d", &P);
  m = log (P) / log (2);
  t = 0;
  if (m % W > 0)
    {
      t = m / W + 1;
    }
  else
    t = m / W;
    
  while (1)
    {
      printf ("\n%-30s__________________________________________________\n",
	      "");
      printf ("%-30s|_____________________MENU_______________________|\n",
	      "");
      printf ("%-30s|1. Mot so chua duoc bieu dien dang mang         |\n",
	      "");
      printf ("%-30s|2. Da duoc bieu dien                            |\n",
	      "");
      printf ("%-30s|________________________________________________|\n",
	      "");
      printf ("%-30sMoi ban chon chuc nang \n", "");
      int chon;
      scanf ("%d", &chon);

      switch (chon)
	{
	case 1:
	  
	  printf ("Nhap so a :");
	  scanf ("%d", &a);
	  int *pA = PAr (a);
	  int A[100];
	  for (int i = 0; i < t; i++)
	    {
	      A[i] = pA[i];
	    }
	 
	  printf ("Nhap so b :");
	  scanf ("%d", &b);
	  int *pB = PAr (b);
	  int B[100];
	  for (int i = 0; i < t; i++)
	    {
	      B[i] = pB[i];
	    }
	    phep_tinhnhan(A,B);
	 
	     
	  break;
	case 2:
	  printf ("Nhap mang a: ");
	  
	  for (int i = t-1; i >=0 ; i--)
	    {
	      printf ("A[%d]= ",i);
	      scanf ("%d", &A[i]);
	    }
	  printf ("Nhap mang b: ");
	  
	  for (int j = t-1; j >= 0; j--)
	    {
	      printf ("B[%d]= ",j);
	      scanf ("%d", &B[j]);
	    }
	  phep_tinhnhan(A,B);
	break;
	}
    }
}
