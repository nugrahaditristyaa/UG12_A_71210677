kata = str(input("Input : "))
lebar = len(kata)
print("Output :",end="")
for baris in range (0,lebar,1) :
    for kolom in range(0,baris,1) :
        print (kata[kolom],end="")
    print ("")
for baris in range (lebar,0,-1) :
    for kolom in range (0,baris) :
        print(kata[kolom],end="")
    print ("")
