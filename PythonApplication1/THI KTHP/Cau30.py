import math
def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def is_carmichael(n):
    if n<=1 or is_prime(n):
        return False
    for a in range(3,n,2):
        if math.gcd(a,n)==1:
            if a**(n-1)%n!=1:
                return False
    return True
def tinhtong(N):
    list=[]
    s=0
    for i in range(N):
        if is_carmichael(i):
            list.append(i)
    for i in list:
        s+=i
    print("Tong so Carmichael nho hon %d la %d"%(N,s))
while(1):
    N=int(input("Nhap so N 0<=N <=10000 : "))
    if( 0<=N<=10000):
        break
tinhtong(N)