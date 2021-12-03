#Mengambil inputan
a1 = input("Masukkan deret angka : ")
a2 = a1.split(",")
calculate = len(a2)
if(int(a2[0]) % 2 == 0):
   aa = a2[0]
   sum = int(aa)
else:
    aa = int(a2[0]) * - 1
    sum = int(aa)
print("Total : " , aa ,end="  ")
for bb in a2[1:calculate]:
    if(bb != a2[0]):
        if(int(bb) % 2 == 1):
            bb = int(bb) * - 1
            sum = sum + int(bb)
            print(" ", bb ,end=" ")
        elif(int(bb) % 2 == 0):
            sum = sum + int (bb)
            if (bb == a2[0]):
                print(bb ,end=" ")
            else:
                print(" + ", bb ,end=" ")
print()
print("Hasil perhitungan diatas ialah",sum)


