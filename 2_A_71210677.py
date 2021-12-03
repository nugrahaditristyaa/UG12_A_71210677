#variable
a1 = []
a2 = []

#Operasi dan Input
while(True):
    aa = input("Masukkan nama: ")
    if aa == "STOP":
        break 
    bb = input("Masukkan nomor kursi "+aa+": ")
    if bb == "STOP":
        break
    if bb in a2:
        print("Mohon maaf kursi telah terisi!")
    elif bb not in a2:
        a1.append(aa)
        a2.append(bb)

#Output       
print()
print("List kursi yang telah terisi : ")
for contents in range(0, len(a2), 1):
    print("Kursi nomor", a2[contents], "telah diisi oleh", a1[contents])
    
