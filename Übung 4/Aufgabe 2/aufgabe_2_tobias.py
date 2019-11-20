def intSuperliste(testedIntSuperliste):
    if type(testedIntSuperliste) != type([]):
        return False
    else:
        subList=True
        if testedIntSuperliste == []: return False
        for element in testedIntSuperliste:
            if type(element) == type([]):
                subList= subList and intSuperliste(element) # [[1],[1]]
            elif type(element) == type(1):
                pass
            else:
                return False
        return subList
#    print(intSuperliste()) [[1],[1]] [[1,"a"],[1]] [[1,[]],[1]]
#print(intSuperliste([[1],[1]]))
#print(intSuperliste([[1,"a"],[1]]))
#print(intSuperliste([[1,[]],[1]]))

def Kopie(intSuperliste):
    out = []
    iSlShallowCopy= intSuperliste[:]
    while iSlShallowCopy != []:
        element = iSlShallowCopy.pop(0)
        if type(element) == type(1):
            out.append(element)
        elif type(element) == type([]):
            out.append(Kopie(element))
    return out
#k=[x for x in range(3)]
u=[[],[[1,2,3,0]],[1]]
while u != []:
    print(u)
    print(u.pop(0))
u=[[],[[1,2,3,0]],[1]]
print(Kopie(u))
l=Kopie(u)
u.append([1])