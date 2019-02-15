x = 1
max = 0
while x!=0 :
    if x > max :
        max = x
    x = int(input("Masukan bilangan : "))
    if x == 0 :
        break
print("Bilangan terbesar adalah : ",max)

