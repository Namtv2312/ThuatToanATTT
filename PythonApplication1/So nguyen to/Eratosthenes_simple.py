import math
def Eratothenes_spl(n):
    
 #prime=[True for i in range(n+1)]
 #p=2
 #while (p*p <=n):
 #   if (prime[p]==True):
 #       for i in range (p*2,n+1,p):
 #           prime[i]=False
 #   p+=1
 #prime[0]=False
 #prime[1]=False
 #for p in range(n+1):
 #   if prime[p]:
 #       print (p)
 p=2
 list=[i for i in range(2,n+1,1)]
 l=[i for i in range(2*p,n+1,p)]
 while (len(l)!=0): #while(p*p<=n)
     l=[i for i in range(2*p,n+1,p)]
     list=[i for i in list if i not in l]
     p=min(i for i in list if i>p)    
 for i in list:
    print(i)
 return list
Eratothenes_spl(100)