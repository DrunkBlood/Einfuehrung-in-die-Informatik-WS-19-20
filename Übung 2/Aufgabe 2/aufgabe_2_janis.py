z=input("Geben sie eine Zeichenkette ein: ")
x=int(input("Geben sie eine Zahl ein, um welche die Zeichenkette verschoben werden soll: ")) #x<=0
fin= " "
for char in z:
    y=ord(char)
    y=y+x
    fin=fin+chr(y%128)
print(repr(fin))
    