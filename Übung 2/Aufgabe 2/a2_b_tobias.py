string= input("Zeichenkette: ")
x= int(input("Integer: ")) # Verschiebung
erg= ""
i=0
k=0
skipNextOne=False
skipNextThree=False
for char in string:
    uni= ord(char)
    if uni == 92:
        if ord(string[string.index(char,k)+1]) == 92:
            uni = 92
            skipNextOne=True
        elif ord(string[string.index(char,k)+1]) == ord("t"):
            uni = 9
            skipNextOne=True
        elif ord(string[string.index(char,k)+1]) == ord("n"): 
            uni = 10
            skipNextOne=True
        elif ord(string[string.index(char,k)+1]) == ord("r"): 
            uni = 13  
            skipNextOne=True
        else:
            uni = ord(chr(int(string[string.index(char,k)+2]+string[string.index(char,k)+3])))
            skipNextThree=True
    uni-=x
    if i<=0:
        erg+=chr(uni%128)
    i-=1
    if skipNextOne:
        skipNextOne=False
        i=1
    if skipNextThree:
        skipNextThree=False
        i=3
    k+=1
print(repr(erg))
    
#for i in range(128):
    #print(i,":", repr(chr(i)))