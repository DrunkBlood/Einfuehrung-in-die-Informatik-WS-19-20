def find_pos (zeichen,buchstabe): 
    l=0
    if zeichen == "":
        return(-1)
    if zeichen != "":
        for char in zeichen:
            if char == buchstabe:
                print(zeichen)
                return(l)
            l=l+1
    for char in zeichen:
        if char != buchstabe:
            return(-1)
    
zeichen=input(str("Zeichenkette : " ))
buchstabe=input("Buchstabe : " )

out1= find_pos(zeichen,buchstabe)
print(out1)
#Teilaufgabe a

f=open("de_DE_frami.txt")
#for line in f:
   # print(line

for ind in f:
    


f.close()

