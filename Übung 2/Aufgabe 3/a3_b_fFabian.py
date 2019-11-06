fin: bool = False
while not fin:
    Bzahl: str = input("Dezimalzahl")
    Fehler : bool = False
    KEintrag = False
    if Bzahl == "" :
        print("Keine Dezimalzahl")
        KEintrag = True
    if not KEintrag :
        for char in Bzahl :
            if not (ord(char) >= 48 and ord(char) <= 57): Fehler = True
        if Fehler :
            print ("Keine Dezimalzahl")
        else:
            fin = True
k = 0
leer: str = ""
kBinzahl = int(Bzahl)
while kBinzahl >= 2 ** k:
    k += 1
if kBinzahl == 0: k += 1
while k > 0:
    if kBinzahl - 2 ** (k - 1) >= 0:
        leer += "1"
        kBinzahl = kBinzahl- (2 ** (k - 1))
    else:
        leer += "0"
    k = k - 1
print("Leer")
