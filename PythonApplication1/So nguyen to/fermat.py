#input n le >=3
import random
def fermat(n,t):
    for i in range (1,t):
        a=random.randrange(2,n-1,1)
        r=modu(a,n-1,n)
        if r!=1:
            return True, "Hop so"
        else:return False, "Nguyen to"
def convertbin(n):
    bin=[]
    while n!=0:
        bin.append(n%2)
        n//=2
    return bin
def modu(a,k,n):
    b=1
    t=len(convertbin(k))
    K=convertbin(k)
    if k==0:
        return b
    A=a
    if int(K[0])==1:
        b=a
    for i in range(1,t):
        A=(A**2) %n
        if K[i]==1:
            b=(A*b) %n
    return b
print(convertbin(25))
print(fermat(7,4))