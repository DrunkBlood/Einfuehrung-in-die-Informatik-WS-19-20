b = input("Zeichenkette").lower()
vokal = input("Vokal")
for txt in b:
    if txt == "a" or txt == "e" or txt == "i" or txt == "o" or txt == "u":
        ind = b.index(txt)
        b = b[:ind] + vokal + b[ind + 1:]
print(b)
