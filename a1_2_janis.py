n = open("dictionary.txt")
x = input("Zeichenkette : ")
l=0
line = n.readline()
while line != "":
    l=l+1
    if x in line:
       break
    line = n.readline()
    print(l)
n.close()
        
        