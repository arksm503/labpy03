import random

n = int(input("Masukan nilai N : "))
for i in range(n) :
    a=random.uniform(0.0,0.5)
    print ("data ke : ", i, "=> ", a)
print("Selesai")