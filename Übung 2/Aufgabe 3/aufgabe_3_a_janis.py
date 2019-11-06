x=int(input("Geben sie eine Zahl ein: ")) #input
bin=2                                     #system you want to change
egsum=" "
if x > 0:
    for i in range(x**2):
        eg=x%bin
        x=x//bin
        egsum=str(eg) + egsum
        if x < 1:
            break
               
    print(egsum)
else:
    print("mistakes were done, try again")