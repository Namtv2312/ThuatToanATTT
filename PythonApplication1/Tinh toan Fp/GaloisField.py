from galois_field import GFpn 

# Generating the field GF(2^4)
# irreducible polynomial. (in this case, x^4 + x+1)
import sys
print("FORM FORMAT: ax^3 + bx^2 +cx +d ...")
a=[int(i) for i in input("Nhap a(x): ").split()]
b=[int(i) for i in input("Nhap b(x): ").split()]
p=[int(i) for i in input("Nhap g(x): ").split()]

if (len(sys.argv)>1):
  a=eval("["+sys.argv[1].replace(" ","")+"]")
if (len(sys.argv)>2):
  b=eval("["+sys.argv[2].replace(" ","")+"]")
if (len(sys.argv)>3):
  p=eval("["+sys.argv[3].replace(" ","")+"]")
try:  
  gf = GFpn(2,p )
except Exception as e:
  print ("Error:" ,e)
  sys.exit()

# Generating an element in GF(2^4)
aval = gf.elm(a)  # x^2+x+1
bval = gf.elm(b) # x

# Arithmetic operations
aval + bval # 1x^2 + 1
aval - bval # 1x^2 + 1
aval * bval # 1x^3 + 1x^2 + 1x
aval / bval # 1x^3 + 1x

print ("a:\t\t",aval)
print ("b:\t\t",bval)
print ("b^{-1}: ",bval.inverse())
print ("p:\t",gf,p)

print ("\nAdd:\t\t",aval + bval)
print ("Subtract:\t",aval - bval)
print ("Multiply:\t",aval * bval)
print ("Divide:\t\t",aval / bval)
