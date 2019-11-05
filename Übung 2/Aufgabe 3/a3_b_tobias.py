done=False
while not done:
    binZ=input("Dezimalzahl: ")
    error=False
    empty=False
    if binZ=="":
        print("FEHLER: Die Eingabe ist keine Dezimalzahl")
        empty=True
    if not empty:
        for char in binZ:
            if not(ord(char)>=48 and ord(char) <= 57): error=True
        if error:
            print("FEHLER: Die Eingabe ist keine Dezimalzahl")
        else:
            done=True
#find k
k=0
out=""
ibinZ=int(binZ)
while ibinZ>=2**k:
    k+=1
if ibinZ==0:k+=1
#print(k)
while k>0:
    if ibinZ-2**(k-1)>=0:
        out+="1"
        ibinZ-=2**(k-1)
    else:
        out+="0"
    k-=1
print (out)