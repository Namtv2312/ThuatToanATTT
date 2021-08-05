#input hop so nhung k phai luy thua cua so nguyen to nao
def gcd(a,b):
    if a==0:
        return b
    else: return gcd(b%a,a)
def rho(n):
    a=2;b=2
    while(1):
        a=(a*a+1)%n
        b=(b*b+1)%n
        b=(b*b+1)%n
        d=gcd(a-b,n)
        if 1<d <n :
            return True,d
        elif d==n:
            return False
print(rho(43567127))
