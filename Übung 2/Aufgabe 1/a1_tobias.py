x=input("Zeichenkette: ").lower()
vok=input("Vokal: ") # a e i o u
for char in x:
    if char in "aeiou":
        ind=x.index(char)
        x= x[:ind]+vok+x[ind+1:]
print(x)
