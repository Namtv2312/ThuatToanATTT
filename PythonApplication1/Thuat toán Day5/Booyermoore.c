#include <stdio.h>
#include <string.h>
int Last_Occerence(char p[],char t)
{
    int k,i=0;
    for(i=strlen(p)-1;i>=0;i--)
    {
        if(p[i]==t)
        {
            k=1;
            break;
        }
    }
    if(k){
        return i;
    }
    else return -1;
}
int min(int a, int b) 
{
    return (a>b)? b:a;
}/*
void preLast(char T[],char P[],int *i,int *j){
    *i=i+strlen(P)-min(j,1+Last_Occerence(P,T[i]));
    *j=strlen(P)-1;
}*/
void booyer_moore(char T[],char P[])
{
    int check=0;
    int i,j;
    i=strlen(P)-1;
    j=strlen(P)-1;
    int count=0;
    int operato=0;
    int loop =0;
    while(i<strlen(T))
    {
        if(T[i]==P[j]){
            operato++;
            count++;
            i--;
            j--;
        }
        else{
            operato++;
            loop++;
            count=0;
            i=i+strlen(P)-min(j,1+Last_Occerence(P,T[i]));
            j=strlen(P)-1;
        }
        if(count==strlen(P)){
            check=1;
            printf("Thay o vi tri %d\n",i+1);
            printf("So phep toan %d\n",operato);
            printf("So vong lăp %d\n",loop);
        }
    }
    
    if(check!=1)
    {
            printf("\nKhong tim thay");
            printf("\nSo phep toan %d",operato);
            printf("\nSo vong lap %d",loop);
    }
}
int main()
{
    char T[]="a pattern matching algorithm";
    char P[]="rithm";
    booyer_moore(T,P);
}