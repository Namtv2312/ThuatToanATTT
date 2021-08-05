import math
W=0; p=0
W=int(input("W= "))
p=int(input("p= "))
m=math.ceil(math.log2(p))
t=math.ceil(m/W)

def arA(a):
    A=[]
    for i in range(t-1,-1,-1):
        A.append(math.floor(a/2**(i*W)))
        a=a%2**(i*W)
    return A
def ar_to_num(A):
    a=0
    A.reverse()
    for i in range(0,t):
        a+=A[i]*2**(i*W)
    return a
def multi_add(a,b):
    ep_si=0
    c=[0]*t
    for i in range(0,t):
        c[i]=a[i]+b[i]+ep_si
        if( 0 <= c[i] < 2**W):
            ep_si=0
        else:
            ep_si=1
        c[i]=c[i]%2**W
        #ep_si=0 if( 0<=a[i]+b[i] +ep_si and a[i]+b[i] +ep_si<=2**W) else 1
    #print("(%d,"%ep_si +'('+','.join(str(int(x)) for x in c)+'))')
    return (ep_si,c)
    
def multi_sub(a,b):
    ep_si=0
    c=[0]*t
    for i in range(0,t):
        c[i]=a[i]-b[i]-ep_si
        #if( 0 <= c[i] < 2**W):
        #    ep_si=0
        #else:
        #    ep_si=1
        c[i]=c[i]%2**W
        ep_si=0 if 0<=a[i]-b[i] -ep_si<=2**W else 1
    print("(%d,"%ep_si +'('+','.join(str(int(x)) for x in c)+'))')
    return(ep_si,c)
def addFp(a,b):
    F=multi_add(a,b)[0:2]
    if F[0]==1:
        multi_sub(F[1],arA(p))
    elif ar_to_num(F[1])>=p:
        multi_sub(F[1],arA(p))
    else: multi_add(a,b)
def subFp(a,b):
    F=multi_sub(a,b)
    if F[0]==1:
        multi_add(F[1],arA(p))
    else: multi_sub(a,b)
a=int(input("a= "))
###print("\n".join(str(x) for x in arA(a).values()))
##for  i  in range(len(arA(a))):
##                 print(arA(a)[i])
b=int(input("b= "))
##print("".join(str(W)+str(p)+str(m)+str(t)))
#print(" ".join(str(x) for x in arA(a)))
#print(" ".join(str(x) for x in arA(b)))
#print(ar_to_num(arA(a)))
#A=[int(x) for x in input("Nhap A").split()]
#B=[int(x) for x in input("Nhap B").split()]
#multi_add(A,B)
#multi_sub(A,B)
addFp(arA(a),arA(b))

