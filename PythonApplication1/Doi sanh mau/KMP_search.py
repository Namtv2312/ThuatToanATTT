#Thuật toán KMP _search
import string
def pre_suffix(j,P):
    pre=[]
    suff=[]
    p='';s=''
    for i in range(j):
        p+=P[i]
        pre.append(p)
    for i in range(j-1,0,-1):
        s=P[i]+s
        suff.append(s)
    return pre,suff
def failture_FC(P):
    #P.translate({ord(c): None for c in string.whitespace})
    #F=[0]*(len(P))
    #F[0]=-1
    #i=2
    #j=0
    #for i in range(2, len(P)):
    #    if(P[i-1]==P[j]):
    #        F[i]=j+1
    #        i+=1
    #        j+=1
    #    elif j>0 :
    #        j=F[j]
    #    else:
    #        F[i]=0
    #        i+=1
    #return  F
    F=[0]*len(P)
    F[0]=-1
    for i in range(2,len(P)):
        suff=pre_suffix(i,P)[1]
        pre=pre_suffix(i,P)[0]
        common=list(set(pre).intersection(suff))
        try:
            F[i]=max(len(i) for i in common)
        except ValueError:
            F[i]=0  
    return F


def KMP(T,P):
    F=failture_FC(P)
    k=0 #bien tam thoi, để thay cho i, vì i không thay đổi
    i=0
    j=0
    loop=0
    operator=0
    count=0
    try:
     while i<len(T):
        if T[k]==P[j]:
            operator+=1
            count+=1
            k+=1
            j+=1
        else:
            loop +=1
            operator+=1
            i=i+j-F[j]
            j= F[j] if F[j]!=-1 else 0
            k=i
            count=j
        if(count==len(P)):
               return True, k-len(P), loop, operator
    except IndexError:
        return False, loop, operator

       
T=input("Nhập chuỗi đầu vào: ")
P=input("Nhập chuỗi đối sánh: ")
if KMP(T,P)[0]:
    print(f"Thay o vi tri: {KMP(T,P)[1]}")
    print(f"Số phép toán {KMP(T,P)[3]}")
    print(f"Số vòng lặp {KMP(T,P)[2]}")
else :
    print("Khong tim thay")
    print(f"Số phép toán {KMP(T,P)[2]}")
    print(f"Số vòng lặp {KMP(T,P)[1]}")
