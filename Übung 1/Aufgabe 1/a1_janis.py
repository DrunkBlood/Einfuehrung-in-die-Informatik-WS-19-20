#nummer 1
a=int (input("Geben sie die Höhe ihres Rechtecks ein "))
b=int (input("Geben sie die Breite ihres Rechtecks ein "))

n=0
c=a*b
cab=str(c)

print(" " + "-"*a)

for n in range (0,b,1):
    print("|" + " "*a + "|")
print(" " + "-"*a)

print("Ihr Rechteck ist " + cab + " quadratmeter groß")





