x=int(input("Geben sie eine Zahl ein: ")) #input
bin=2                                     #system you want to change
egsum=" "
f=0

for char in str(x):
    if char in "0123456789":
        f=1
    
    
if x==0:
    print("0")

if x >= 0 and f==1:
    for i in range(x**2):
        eg=x%bin
        x=x//bin
        egsum=str(eg) + egsum
        if x < 1:
            break
               
    print(egsum)

else:
    print("mistakes were done, try again")