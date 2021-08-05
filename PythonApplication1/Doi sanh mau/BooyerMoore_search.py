#thuat toan booyer moore_ NamST
'''def Last_occerence(T,P):
    in_dex=len(P)-P.reverse().index(T)-1 #len(P)-P[::-1].index(T)-1
    return in_dex'''
def preLast(T,P,i,j):
    i=i+len(P)-min(j,1+P.rfind(T[i]))
    j=len(P)-1
    return i,j
def booyer_moore(T,P):
   i=len(P)-1
   j=len(P)-1
   count=0 #TINH SO KY TU TRUNG KHOP
   operator=0
   loop=0
   while(i<len(T)):
       if(T[i]==P[j]):
           operator+=1
           count+=1
           i-=1
           j-=1          
       else:
           operator+=1
           loop+=1
           count=0
           ij=preLast(T,P,i,j)
           i=ij[0]
           j=ij[1]
       if(count==len(P)):
           return True, i+1, loop, operator
   if( count !=len(P)): return False, loop, operator
       
T=input("Nhập chuỗi đầu vào: ")
P=input("Nhập chuỗi đối sánh: ")
if booyer_moore(T,P)[0]:
    print(f"Thay o vi tri: {booyer_moore(T,P)[1]}")
    print(f"Số phép toán {booyer_moore(T,P)[3]}")
    print(f"Số vòng lặp {booyer_moore(T,P)[2]}")
else :
    print("Khong tim thay")
    print(f"Số phép toán {booyer_moore(T,P)[2]}")
    print(f"Số vòng lặp {booyer_moore(T,P)[1]}")
