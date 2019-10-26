height=int(input("Geben Sie a ein:"))
width=int(input("Geben Sie b ein:"))
print(" " + "-"*width + " ")
for i in range(height):
    print("|"+ " "*width + "|")
print(" " + "-"*width + " ")