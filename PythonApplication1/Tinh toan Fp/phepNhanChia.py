import math
global W, p
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
def phepNhan(a,b):
    c=[0]*2*t
    for i in range(t):
        c[i]=0
    for i in range (t):
        U=0;UV=0
        for j in range (t):
            UV=c[i+j]+a[i]*b[j]+U
            U=UV//256
            c[i+j]=UV%256
        c[i+t]=U
    print("c= ("+ ", ".join(str(x) for x in c[::-1])+")")
A=[int(a) for a in input("Nhap A:").split()]
B=[int(b) for b in input("Nhap B:").split()]
A.reverse()
B.reverse()
phepNhan(A,B)

