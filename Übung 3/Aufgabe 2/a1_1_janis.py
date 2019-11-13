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
f=open("de_DE_frami.txt")
n = open("dictionary.txt","w")
line = f.readline()
i = 0
while line != "":
    if "#" not in line:
        if "\t\n" not in line:
            for slash in line:
                if slash == "/":
                    slashindex = line.index(slash)
                    line = line[0:slashindex]
                    line = line + "\n"
         n.write(line)   
    line = f.readline()
f.close()
n.close()
print("bin feddisch alda")

