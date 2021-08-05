import math
r1=[1,1,0,1]
r2=[1,1,1]
def getDegree(a):
    global deg
    for i in range(len(a)):
        if a[i] != 0:
            deg = i
    return deg
def doDivision(a1,b1):
    
    # Initialize quotient list with 0s of size as r1
    # Khởi tạo mảng số thương độ dài r1
    qq = [0]*len(r1)
    
    ai = getDegree(a1)
    bj = getDegree(b1)    
    
    while ai >= bj and 1 in a1:
        t_pow = ai-bj
        t_coeff = a1[ai]/b1[bj]
        
        qq[t_pow] = t_coeff
        
        # Initializing temporary list for intermediate products
        t_mul = [0]*len(r1)
        
        # Multipliying divisor with quotient
        for i in range(bj+1):
            t_mul[i+t_pow] = b1[i]*t_coeff
            
        # New intermediate dividend
        for i in range(len(a1)):
            a1[i] = math.fmod(a1[i] - t_mul[i],2)
                 
        ai = getDegree(a1)
    
    return qq, a1

print(doDivision(r1,r2)[0])
print(doDivision(r1,r2)[1])