def BruteForce(T,P):
    loop=0
    operator=0
    n=len(T)
    m=len(P)
#'''   for i in range(n-m+1):
#        j=0;
#        while j<m and T[i+j]==P[j]:
#            operator+=1
#            j=j+1
#        if j==m:
#            #return True,i,loop,operator
#        else:
#            loop+=1
#            operator+=1
#    #return False, loop, operator
    for i in range(n):
        k = i 
        for j in range(m):
            if P[j] == T[k]:
                operator+=1 #phep so sanh
                if j == len(P)-1:
                    return True, i,loop,operator 
                else :
                    k+=1
                    operator+=1 #phep tang i
            else:
                operator+=1 #phep so sanh khong bang
                loop+=1
                break
    return False, loop, operator


T=input("Nhập chuỗi đầu vào: ")
P=input("Nhập chuỗi đối sánh: ")
if BruteForce(T,P)[0]:
    print(f"Thay o vi tri: {BruteForce(T,P)[1]}")
    print(f"Số phép toán {BruteForce(T,P)[3]}")
    print(f"Số vòng lặp {BruteForce(T,P)[2]}")
else :
    print("Khong tim thay")
    print(f"Số phép toán {BruteForce(T,P)[2]}")
    print(f"Số vòng lặp {BruteForce(T,P)[1]}")
