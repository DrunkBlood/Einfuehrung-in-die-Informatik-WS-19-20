def find_pos(string,char):
    if char in string:
        return string.index(char)
    else:
        return -1
#print(find_pos("Abbild/JRTSm","/"))
#print(find_pos("Abbild/JRTSm","0"))
dictDE = open("de_DE_frami.dic",'r')
dictErg = open("dictionary.txt", 'w')
#i=0
for line in dictDE:
    #if i>100:break
    #i+=1
    if find_pos(line,'#') == -1:
        if line != "\t\n":
            if '/' in line:
                dictErg.write(line.split("/")[0]+"\n")
            else:
                dictErg.write(line)
dictDE.close()
dictErg.close()