def baum(h):
    if ((h-34) <= 0) and (((h-11)/2)  < 0):
        return h
    else:
        if baum(h-34) > baum((h-11)/2) and baum(h-34) < 0:
            return baum(h-34)
        else:
            return baum((h-11)/2)

x=float(input("Baumhöhe des höchsten Baumes : "))
print("Der Baum ist " + str(baum(x)) +" Meter hoch")