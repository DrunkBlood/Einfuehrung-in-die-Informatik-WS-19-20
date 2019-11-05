string= input("Zeichenkette: ")
x= int(input("Integer: ")) # Verschiebung
erg= ""
for char in string:
    uni= ord(char)
    uni+= x
    erg+= chr(uni%128)
print(repr(erg))