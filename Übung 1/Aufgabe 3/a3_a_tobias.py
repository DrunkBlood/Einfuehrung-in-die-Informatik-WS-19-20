x= int(input("x:")) # 0<=x<=23 x ist ganz STUNDEN
y= int(input("y:")) # 0<=y<=59 y ist ganz MINUTEN
z= int(input("z:")) # 0<=z     z ist ganz MINUTEN NACH ABFLUG
#(i)
xy= x*60 + y # alle Mins
xy-=z # Startzeit in Mins
if xy < 0: xy+=24*60
#print(str(xy//60)+":"+str(xy%60))
if xy//60 < 10:
    h= "0"+str(xy//60)
else:
    h=str(xy//60)
if xy%60 < 10:
    m= "0"+str(xy%60)
else:
    m=str(xy%60)
print("(i)"+h+":"+m)
#(ii)
xy-=30
if xy<0:xy+=24*60
if xy//60 < 10:
    h= "0"+str(xy//60)
else:
    h=str(xy//60)
if xy%60 < 10:
    m= "0"+str(xy%60)
else:
    m=str(xy%60)
print("(ii)"+h+":"+m)