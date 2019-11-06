x=int(input("Geben sie eine Zahl ein: ")) #input
bin=10                                     #system you want to change
l=len(str(x))
erg=0
f=1

for char in str(x):
    if char in "23456789":
        print("dies ist keine Binärzahl")
        f=0
        break

for i in str(x):
    l=l-1
    h=int(i)*2**(l)
    erg=erg + h 

    
    if l==0 and f==1 :
        print(str(erg))
        break
    
    
  
    
        
        
        
        
    
     
        