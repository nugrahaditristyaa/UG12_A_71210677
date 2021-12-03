#Mengambil input
a1 = int(input("Input : "))
a2 = 2
print ("Output : ")
for aa in range (1,a1+1):
    for bb in range (1,2*a1) :
        if aa+bb==a1+1 or bb-aa==a1-1:
            print ("*", end="")
        elif aa==a1 and bb!= a2:
            print ("*",end="")
            a2 = a2 + 2
        else:
            print (end=" ")
    print ()
  
