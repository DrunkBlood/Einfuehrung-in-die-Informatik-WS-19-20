#TODO finde geeignete Startwerte
def findCubeRoot(w,e):
    def findIntCubeRoot(i,e):
        left=0
        right=i
        val=(left+right)/2
        while abs(val**3-i)>=e:
            if val**3<i:
                left=val
            else:
                right=val
            val=(left+right)/2
        return val
    if not e>0 or not type(e) == type(0.0):
        print("Fehler: epsilon ist nicht im Parameterbereich")
        return
    if not type(w) == type(0.0):
        print("Fehler: w ist nicht im Parameterbereich")
        return
    #print("Parameter sind ok")
    addMinus=False
    if w<0: 
        w*=-1
        addMinus=True
        #print(w)
    wstr=str(w)
    zaehler=int(w*10**len(wstr.split(".")[1]))
    nenner=10**len(wstr.split(".")[1])
    erg=findIntCubeRoot(zaehler,e)/findIntCubeRoot(nenner,e)
    if addMinus:erg*=-1
    return erg
print(findCubeRoot(float(input("float ")),float(input("eps "))))