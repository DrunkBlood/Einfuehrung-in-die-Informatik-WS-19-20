done=False
while not done:
    binZ=input("Binärzahl: ")
    error=False
    empty=False
    if binZ=="":
        print("FEHLER: Die Eingabe ist keine Binärzahl")
        empty=True
    if not empty:
        for char in binZ:
            if char != "0" and char != "1": error=True
        if error:
            print("FEHLER: Die Eingabe ist keine Binärzahl")
        else:
            done=True
binZint=int(binZ)
erg=0
i=0
for zif in binZ:
    erg+=int(zif)*2**((len(binZ)-1)-i)
    i+=1
    #print(int(zif),2**(len(binZ)-1-binZ.index(zif)),len(binZ)-1-binZ.index(zif),len(binZ),-1-binZ.index(zif))
print(erg)