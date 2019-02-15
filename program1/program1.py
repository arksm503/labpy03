m = 100000000
sum = 0
j = 0
lb = [int(0), int(0), int(m) * .1, int(m) * .1, int(m) * .5, int(m) * .5, int(m) * .5, int(m) * .2]
print("Modal Awal               :",m)
for i in lb :
    sum = sum + i
    j +=1
    print("laba bulan ke-", j ,"sebesar :", i )

print("Total laba adalah        :", sum)
