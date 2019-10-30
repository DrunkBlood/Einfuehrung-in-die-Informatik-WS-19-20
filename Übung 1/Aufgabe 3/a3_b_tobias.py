h=int(input("Stunden:"))
m=int(input("Minuten:"))
hm= h*60 + m
hm-= 7*60
if hm < 0: hm+= 24*60
if hm//60 < 10:
    hout= "0"+str(hm//60)
else:
    hout=str(hm//60)
if hm%60 < 10:
    mout= "0"+str(hm%60)
else:
    mout=str(hm%60)
print(hout+":"+mout)
