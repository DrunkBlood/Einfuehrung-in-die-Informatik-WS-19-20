wort = input("Wort: ")
dictR = open("dictionary.txt",'r')
lineNr=1
for line in dictR:
    if wort == line[:-1]:
        print(lineNr)
        break
    lineNr+=1
dictR.close()