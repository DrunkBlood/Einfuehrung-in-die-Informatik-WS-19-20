def maximiere(x,k):
    def sortiere(s):
        return "".join((sorted(s)[::-1]))
    
    def vertausche(s,i,j):
        return s[0:i]+s[j]+s[i+1:j]+s[i]+s[j+1:len(s)]
    
    s=sortiere(x)
    if k== 0:
        return x
    
    elif x == s:
        return x
    
    else:
        for char in x[::-1]:
             if x[x.index(char)] == s[k-1] and char != x[k-1]:
                return maximiere(vertausche(x,k-1,x.index(char)),k-1)

x=str("223953")
k=2
print(maximiere(x,k))