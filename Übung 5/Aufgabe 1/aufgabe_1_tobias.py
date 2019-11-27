def maximiere(s,k):
    def vertausche(s,i,j):
        return s[0:i]+s[j]+s[i+1:j]+s[i]+s[j+1:len(s)]

    def sortiere(s):
        return "".join((sorted(s)[::-1]))

    if x == sortiere(x) or k == 0:
        return x
    else:
        maxNum=max(set(x))
        maxNumIndex=x.index(maxNum)
        if maxNumIndex != 0:
            return maximiere(vertausche(x,0,maxNumIndex),k-1)
        else:
            return maxNum + maximiere(x[1:],k)