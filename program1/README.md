1.) m = 100000000
 modal 100,000,000, variable m

2.) sum = 0
 variable untuk menjumlah total laba

3.) j = 0
 variable untuk masa bulan

4.) lb = [int(0), int(0), int(m) * .1, int(m) * .1, int(m) * .5, int(m) * .5, int(m) * .5, int(m) * .2]
 variable untuk jumlah laba perbulan, dipisahkan dengan koma, tipe data integer

5.) for i in lb :
 looping for indexs i, dengan mengambil data dari lb

6.) sum = sum + i
 rumus untuk menghitung total laba perbulan

7.) j +=1
 masa bulan, tiap looping menambah 1

8.) print("laba bulan ke-", j ,"sebesar :", i )
 print :
    j = ambil masa bulan,
    i = ambil dari data yg ada di dalam lb

9.) print("Total laba adalah :", sum)
 print total laba

<br/>
Berikut Flowchartnya <br/>
![alt text](https://raw.githubusercontent.com/arkyana/labpy03/master/program1/img/flow.png)

<br/>
Berikut Screenshotnya <br/>
![alt text](https://raw.githubusercontent.com/arkyana/labpy03/master/program1/img/ss.png)
