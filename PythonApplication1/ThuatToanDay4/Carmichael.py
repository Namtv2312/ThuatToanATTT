from math import gcd

def is_prime(number):
    if number <= 2:
        return number == 2

    if number % 2 == 0:
        return False

    for divisor in range(3, int(number ** 0.5) + 1, 2):
        if number % divisor == 0:
            return False

    return True

'''
def convert_bin(x):
    bin =""
    while x!=0:
        bin+=str(x%2)
        x=x//2
    return bin
def repeated_squares(a,k,n):
    if k==0:
        return b
    ar=convert_bin(k)
    b=1   
    A=a
    if ar[0]=='1':
        b=a
    for i in range(1,len(ar)):
        A=(A*A) % n
        if ar[i]=='1':
            b=(A*b)%n
    return b
def is_prime(n):
    import random
    a=random.randint(2,n-2)
    if repeated_squares(a,n-1,n)==1:
        return True
    else: return False'''
def is_carmichael(n):
    if n <= 2 or n % 2 == 0 or is_prime(n):
        return False

    for a in range(3, n, 2):
        if gcd(a, n) == 1:
            if pow(a, n - 1, n) != 1:
                return False
    return True
'''
def is_carmichael(n):
    if is_prime(n):
        return False
    else:
        for a in range(1,n):
            if(gcd(a,n))==1:
                if(a**(n-1)%n)!=1:
                    return False
        return True'''
i=0
while i<3: 
    number=int(input("Nhap so: "))
    if is_carmichael(number):
       print ("La so carmichael")
    else :
       print("khong phai")