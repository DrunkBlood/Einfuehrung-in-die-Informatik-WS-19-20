w=float(input("zahl : "))
kleiner=0
groeßer=w
med=(kleiner+groeßer)/2
e=0.01
run=0
if w >= 1:
    while abs(med**3-w)>=e:
        if med**3 > w:
            groeßer=med
        if med**3 < w:
            kleiner=med
        med=(kleiner+groeßer)/2
        run=run+1
        #print("groeßer" + str(kleiner)) #fehlersuche
        #print("kleiner" + str(groeßer)) #fehlersuche
    print("die Kubikwurzel von " +str(w)+ " ist circa " + str(round(med, 8)))
    print("Wir benötigten " +str(run)+ " versuche")
    
if w > 0 and w < 1:#funktioniertnicht...
    print("diese Zahl is zwischen 0 und 1")
    #kleiner=w
    #groeßer=0
    while abs(med**3-w)>=e:
        if med**3 < w:
            groeßer=med
        if med**3 > w:
            kleiner=med
        med=(kleiner+groeßer)/2
        run=run+1
        print("groeßer" + str(kleiner)) #fehlersuche
        print("kleiner" + str(groeßer)) #fehlersuche
            
   
    print("die Kubikwurzel von " +str(w)+ " ist circa " + str(round(med, 8)))
    print("Wir benötigten " +str(run)+ " versuche")
    
if w <= 0:
    w=abs(w)
    groeßer=w
    med=(kleiner+groeßer)/2
    while abs(med**3-w)>=e:
        if med**3 > w:
            groeßer=med
        if med**3 < w:
            kleiner=med
        med=(kleiner+groeßer)/2
        run=run+1
        #print("groeßer" + str(kleiner)) #fehlersuche
        #print("kleiner" + str(groeßer)) #fehlersuche
    print("die Kubikwurzel von -" +str(w)+ " ist circa -" + str(round(med, 8)))
    print("Wir benötigten " +str(run)+ " versuche")

    
    