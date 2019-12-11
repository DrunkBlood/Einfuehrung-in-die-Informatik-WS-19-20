def next_palindrome(num,k):
    while k > 0:
        palindrome = True
        for i in range(len(num) // 2):
            print("in For")
            if num[i] != num[-1 -i]:
                palindrome = False
                break
        #break
        if palindrome:
            k -= 1
            print('palindrome:' + num)
            num = str(int(num) + 1)
        else:
            num = str(int(num) + 1) 

# Die Funktion addiere ist hier nur der Vollständigkeit halber aufgeführt.
def addiere(n,m):
    while n > 0:
        if m > 100:
            print(m)
            break
        else:
            m = m + n
            n = n-1

if __name__ == "__main__":
    # F\"uhren Sie hier den Glass Box Test fuer Funktion next_palindrome durch

    #next_palindrome("23",3) ## schreiben Sie hier was hier abgedeckt wird...
    #while
    next_palindrome("123",0)# Die while-Schleife wird nicht bei k<=0 ausgeführt
    next_palindrome("121",1)# 1 mal
    next_palindrome("123", 1) #kein palindrom und k größer gleich 1
    next_palindrome("121", 2)#palindrom und k größer gleich 2

    #for
    next_palindrome("1", 1)#1 Fall: nicht durchlaufen
    next_palindrome("23", 1)#2 Fall: genau 1 mal durchlaufen
    next_palindrome("223", 1)  # 2 Fall: genau 1 mal durchlaufen
    next_palindrome("2341", 1) # 3 Fall: mehrmals durchlaufen
    next_palindrome("1234", 1) # breakanweisung

    # if in for
    next_palindrome("1234", 1) # True
    # False keine Veränderung == NULL+

    # if nach for
    next_palindrome("1", 1) # True
    next_palindrome("223322", 1) #True
    next_palindrome("22", 1) # True
    next_palindrome("13", 1) # False
    next_palindrome("132", 1) # False

#s = input("num")
#k = int(input("k"))
#print(next_palindrome(s,k))
