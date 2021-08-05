import math
def is_prime(n):
    for i in range(2,int(math.sqrt(n))):
        if n%i==0:
            return False
    return True
def is_carmichael(n):
    if is_prime(n):
        return False
    for a in range(3,n,2):
        if math.gcd(a,n)==1:
            if a**(n-1)%n!=1:
                return False
    return True
def printnum(n):
    for i in range(n):
        if is_carmichael(i):
            print(i)
printnum(10000)
