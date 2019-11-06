fin: bool = False
while not fin:
    BZahl: str = input("Binärzahl")
    Fehler = False
    KEintrag = False
    if BZahl == "":
        print("Keine Binährzahl")
        KEintrag = True
    if not KEintrag :
        for char in BZahl :
            if char != "0" and char != "1" : Fehler = True
        if Fehler :
            print("Keine Binährzahl")
        else:
            fin = True
BZahl = int(BZahl)
Ergebnis = 0
a = 0
for Ergebnis in BZahl:
    a += int(Ergebnis) * 2 ** ((len(BZahl) - 1) - a)
    a += 1
print(Ergebnis)
