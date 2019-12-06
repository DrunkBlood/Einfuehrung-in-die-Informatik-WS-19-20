def zyklisch(wb,i):
    assert type(wb) == dict,'erster Parameter kein Woerter-buch'
    assert type(i) == int, 'zweiter Parameter kein Integer'
    flagInt=True
    for key in wb.keys():
        assert type(key)==int, 'ersterParameter kein int-int Woerterbuch'
        assert type (wb[key]) == int, 'ersterParameter kein int-int Woerterbuch'
    try:
        wb[i]
    except KeyError:
        assert 1 == 0, 'zweiter Parameter kein Schl̈uessel des ersten Parameters'
    Keys=wb.keys()
    Pfad=[]
    k=i
    while i in wb:
        Pfad.append(i)
        if wb[i] in Pfad:
            return True # Lasso
        else:
            i=wb[i]
    return False # kein Lasso
if __name__ == "__main__":
    pass
 
