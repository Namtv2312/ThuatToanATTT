tuoi=0
def cccd(tuoi):
    if tuoi<18:
        raise("Errror",tuoi)
    else: print("Chao nam dep trai")
try:
    cccd(14)
except "Errror":
    print("Lon hon ti nx di")
finally:print("end")