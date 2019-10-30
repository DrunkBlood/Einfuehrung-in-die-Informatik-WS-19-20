a = int(input("Ankunft Stunden:"))
b = int(input("Ankunft Minuten:"))
ab = a * 60 + b
ab: int = ab - 7 * 60
if ab < 0: ab = ab + 24 * 60
if ab // 60 < 10:
    de = "0" + str(ab // 60)
else:
    de = str(ab // 60)
if ab % 60 < 10:
    sdu = "0" + str(ab % 60)
else:
    sdu = str(ab % 60)
print(de + ":" + sdu)
