import math
def tranfer_Array(a):
    global m,p,W,t
    m=math.ceil(math.log(p,2))
    t=math.ceil(m/W)
    A=[]
    for i in range(t-1,-1,-1):
        A.append(a//pow(2,i*W))
        a=a%(pow(2,i*W))
    return A
def addtion(a,b):
    c=[]
    epsil=0
    for i in range(0,t-1):
        c[i]=a[i]+b[i]+epsil
        if (a[i]+b[i]+epsil<0 or a[i]+b[i]+epsil>2**W):
            epsil=1
            c[i]=abs(abs(c[i])-2**W)
        else :epsil =0
    for i in range (0,t-1):
        print(c[i])

p=int(input("Nhap p: "))
W=int(input("Nhap W: "))
a=int(input("Nhap a: "))
b=int(input("Nhap b: "))
ans=True
while ans:
    print ("""
    1.Phép cộng
    2.Phép trừ
    3.Phép nhân
    4. Exit
    """)
    ans=input("Bạn muốn làm gì? ") 
    if ans=="1": 
      addtion(a,b)
    elif ans=="2":
      print("\n Student Deleted") 
    elif ans=="3":
      print("\n Student Record Found") 
    elif ans=="4":
      print("\n Goodbye")
      ans= None
    elif ans !="":
      print("\n Not Valid Choice Try again") 
