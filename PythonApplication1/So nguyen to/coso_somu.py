def coso_somu(n):
    coso=[]
    somu=[]
    for i in range(2,n+1):
        count=0
        while n%i==0:
            count+=1
            n/=i
        if count!=0:
            coso.append(i)
            somu.append(count)
    print("Co so="+str(coso)+","+"So mu="+str(somu))
n=int(input("Nhap n: "))
coso_somu(n)
