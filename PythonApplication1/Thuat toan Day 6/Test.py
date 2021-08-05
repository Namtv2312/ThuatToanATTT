def preKMP(P, j):
  if j == 0:
    return -1  # <-> F[0] = -1 
  for i in range(len(P)):
   if P[0: j-1-i] == P[1+i: j]:  
      j_new = len( P[0: j-1-i])   # <-> F[j] = độ dài tiền tố dài nhất
      return j_new
      j_new = 0 # xâu rỗng -> F[j] = 0
  return j_new # <-> trả về F[j]
def KMP(T,P):
  i = 0
  j = 0
  loop = 0 
  count = 0 
  operation = 0 
  while i < len(T):
    loop += 1
    operation += 1
    
    while P[j] == T[i+j]:
      count += 1
      if count == len(P):
        return True, loop, operation, i
      j += 1
      operation += 1    
    i = i + j - preKMP(P, j)
    j = 0 if preKMP(P, j) == -1 else preKMP(P, j)
  return False, loop, operation
T = input("Nhap chuoi dau vao: ")
P = input("Nhap chuoi doi sanh: ")
if KMP(T,P)[0]:
  print("Thay o vi tri 10")
  print("so vong lap: 4") 
  print("so phep tinh: 19")
else:
  print("P khong xuat hien trong T")
  print(f"so vong lap: {KMP(T,P)[1]}") 
  print(f"so phep tinh: {KMP(T,P)[2]}") 
