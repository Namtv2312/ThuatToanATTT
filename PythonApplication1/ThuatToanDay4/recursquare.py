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
'''def power(x, y, p) :
    res = 1     # Initialize result
 
    # Update x if it is more
    # than or equal to p
    x = x % p
     
    if (x == 0) :
        return 0
 
    while (y > 0) :
         
        # If y is odd, multiply
        # x with result
        if ((y & 1) == 1) :
            res = (res * x) % p
 
        # y must be even now
        y = y >> 1      # y = y/2
        x = (x * x) % p
         
    return res'''
def fermat(n):
        import random
        a=random.randint(2,n-2)
        if repeated_squares(a,n-1,n)!=1:
            print("hop so")
        else : print("Nguyen to")
number=int(input("Nhap so vao: "))
fermat(number)
