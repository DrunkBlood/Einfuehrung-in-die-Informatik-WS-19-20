def Euklid(a,b):
    assert a>0 and b>0, 'Parameter müssen beide positiv sein'
    return Euklid(b,a) if a<b else b if not a%b else Euklid(b,a%b)


def istBruch(x):
    if type(x) == tuple and len(x) == 2 and type(x[0]) == int and type(x[1]) == int and x[1] > 0:
        return True
    else:
        return False

def kuerze(x):
    assert istBruch(x), "Leider handelt es sich um keinen Bruch"
    if (x[0] == 0 and x[1] == 1) or (x[0] != 0 and Euklid(abs(x[0]),x[1])==1):
        return x
    else:
        q = Euklid(abs(x[0]),x[1])
        return ( x[0] // q, x[1]//q)

def plus(x,y):
    assert istBruch(x) and istBruch(y), "Leider handelt es sich nicht umzwei Br̈uche"
    if x[1] != y[1]:
        x = (x[0]*y[1],x[1]*y[1])
        y = (y[0]*x[1],y[1]*x[1])
    #addieren
    erg = (x[0]+y[0],x[1])
    return kuerze(erg)

def minus(x,y):
    assert istBruch(x) and istBruch(y), "Leider handelt es sich nicht umzwei Br̈uche"
    if x[1] != y[1]:
        x = (x[0] * y[1], x[1] * y[1])
        y = (y[0] * x[1], y[1] * x[1])
    # sub
    erg = (x[0] - y[0], x[1])
    return kuerze(erg)

def mal(x,y):
    assert istBruch(x) and istBruch(y), "Leider handelt es sich nicht umzwei Br̈uche"
    return (x[0]*y[0],x[1]*y[1])

def teile(x,y):
    assert istBruch(x) and istBruch(y), "Leider handelt es sich nicht umzwei Br̈uche"
    erg = (x[0]*y[1],x[1]*y[0])
    if erg[1] == 0:
        raise ZeroDivisionError
    if erg[0] == 0:
        return (0,1)
    return kuerze(erg)


if __name__ == "__main__":
    pass


