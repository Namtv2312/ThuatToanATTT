#input n le >=3
import random
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
    for i in range(1,t,1):
        A=(A**2) %n
        if K[i]==1:
            b=(A*b) %n
    return b
def m_rabin(n,t):
    if n==1:
        return False,"Not prime and not composite"
    if(n==2 or n==3):
        return True,"Hop so"
    count=0
    d=n-1
    while d%2==0:
        count+=1
        d/=2
    s=count
    r=d
    
    for i in range(1,t+1):
        a=random.randrange(2,n-1)
        y=modu(a,r,n)
        if y!=1 and y!= -1:
            j=1
            while j<=s-1 and y!=n-1:
                y=(y*y)%n
                if y==1:
                    return True, "Hop so"
                j=j+1
            if y!=n-1:
                return True,"Hop so"
    return False,"Nguyen to"
print(m_rabin(101,1))
