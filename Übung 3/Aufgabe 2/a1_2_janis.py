n = open("dictionary.txt")
x = input("Zeichenkette : ")
l=0
line = n.readline()
while line != "":
    l=l+1
    if x in line:
       print(l)
       break
    line = n.readline()
n.close()
        
        
