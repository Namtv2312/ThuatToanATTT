import math
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def tinhtong(a,b):
    s=0
    for i in range(a,b+1):
        if is_prime(i) is True:
            s+=i
    print("Tong so nguyen to trong doan (%d,%d) = %d"%(a,b,s))
a=int(input("Nhap a: "))
b=int(input("Nhap b: "))
tinhtong(a,b)