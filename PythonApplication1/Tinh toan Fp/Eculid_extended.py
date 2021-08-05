#Input:   Hai sốnguyên dương a, b (a >=bb)
#Output:d = gcd(a, b) và số nguyên x, y thỏa mãn ax + by = d
def gcd(a,b):
    if a==0:
        return b
    else:
        return gcd(b%a,a)
def eculid_Ex(a,b):
    if b==0:
        d=a;x=1;y=0
        return(d,x,y) 
    u=a;v=b
    x1=1;y1=0;x2=0;y2=1
    while u!=0:
        q=v//u;r=v-q*u;x=x2-q*x1;y=y2-q*y1
        v=u;u=r;x2=x1;x1=x;y2=y1;y1=y
    d=v;x=x2;y=y2
    if(d==1):
        print("%d^-1 mod %d = %d"%(a,b,x))
        print("%d^-1 mod %d = %d"%(b,a,y))
    return (d,x,y)
print(eculid_Ex(3458,4864))
def inversionFp(a,p):
    u=a;v=p
    x1=1;x2=0
    while u!=1:
        q=v//u;r=v-q*u;x=x2-q*x1
        v=u;u=r;x2=x1;x1=x
    return x1
print(inversionFp(550,1759))


