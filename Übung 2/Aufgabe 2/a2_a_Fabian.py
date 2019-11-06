Zkette = input("Zeichenkette")
x: int = int(input("Integer"))
fin = ""
for ltr in Zkette:
    a = chr(ltr)
    a += x
    fin += ltr
print(repr(fin))
