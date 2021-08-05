import random
import miller_rabin
import khongtamthuongPollardRho

def rand_search(n,t):
    while(1):
         n=random.randrange(1,1000,1)
         if khongtamthuongPollardRho.rho(n) is True:
             continue
         if miller_rabin.m_rabin(n,t)[0] is False:
             return n,"Nguyen to"
         else: continue
print(rand_search(100,4))

