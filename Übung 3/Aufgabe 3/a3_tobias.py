def lies_Zeile(s):
    stringList = list(s)
    kommata = 0
    for element in stringList:
        if element == ',':
            kommata += 1
    # print(kommata)
    if kommata == 2:
        splitedS = s.split(",")
        return(splitedS[0], splitedS[1], splitedS[2])
    else:
        raise ValueError('Der Parameter s: ' + str(s) + ' enthaelt nicht genau 2 Kommata')
# print(lies_Zeile(input("String")))


def lies_datei(name):
    file = open(name, 'r')
    ret = []
    for line in file:
        line = line[:-1]
        ret.append(lies_Zeile(line))
    file.close()
    return ret
# print(lies_datei("hollywood.csv"))


def hat_schauspieler(FilmTupelListe, schauspieler):
    ret = False
    for filmTupel in FilmTupelListe:
        if filmTupel[1] == schauspieler:
            ret = True
            break
    return ret
#print(hat_schauspieler(lies_datei("hollywood.csv"),"Harrison Ford"))
# print(hat_schauspieler(lies_datei("hollywood.csv"),"Harrison"))


def schauspieler_zusammenarbeit(FilmTupelListe, schauspieler):
    ret = []
    film = []
    if hat_schauspieler(FilmTupelListe, schauspieler):
        for filmTupel in FilmTupelListe:
            if filmTupel[1] == schauspieler:
                film.append(filmTupel[0])
        for filmTupel in FilmTupelListe:
            for f in film:
                if filmTupel[0] == f:
                    if not filmTupel[1] in ret and filmTupel[1] != schauspieler:
                        ret.append(filmTupel[1])
        return ret
    else:
        return []
#print(schauspieler_zusammenarbeit(lies_datei("hollywood.csv"),"Harrison Ford"))
# print(schauspieler_zusammenarbeit(lies_datei("hollywood.csv"),"Harrison"))
#print(schauspieler_zusammenarbeit(lies_datei("hollywood.csv"),"Julianne Morre"))


def fuege_ein(FilmTupelListe, tupel):
    FilmTupelListe.append(tupel)
    FilmTupelListe = sorted(FilmTupelListe, key=lambda FilmTupel: FilmTupel[2])
    return FilmTupelListe
#print(sorted(lies_datei("hollywood.csv"),key=lambda FilmTupel: FilmTupel[2]))
#print(fuege_ein(sorted(lies_datei("hollywood.csv"),key=lambda FilmTupel: FilmTupel[2]),("Jurrasic Park","Laura Dern",input("Regisseure: "))))
