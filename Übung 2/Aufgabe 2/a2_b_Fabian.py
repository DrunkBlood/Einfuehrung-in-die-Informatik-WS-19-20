import string

import k as k

Zkette: str = input("Zeichenkette")
x: int = int(input("Integer"))
fin = ""
a = 0
b = 0
s1 = False
s3 = False
ltr: str
for ltr in Zkette:
    c = chr(ltr)
    if c == 92:
        if chr(string[string.index(ltr, k) + 1]) == 92:
            c = 92
            s1 = True
        elif chr(string[string.index(ltr, k) + 1]) == chr('z1'):
            c = 9
            s1 = True
        elif chr(string[string.index(ltr, k) + 1]) == chr('z2'):
            c = 10
            s1 = True
        elif chr(string[string.index(ltr, k) + 1]) == chr('z3'):
            c = 13
            s1 = True
        else:
            c = chr(int(string[string.index(ltr, k) + 2] + string[string.index(ltr, k) + 3]))
            s3 = True
    c = c - x
    if i <= 0:
        fin += chr(c % 128)
    i = i-1
    if s1:
        s1 = False
        i = 1
    if s3:
        s3 = False
        i = 3
    k += 1
print(repr(fin))
