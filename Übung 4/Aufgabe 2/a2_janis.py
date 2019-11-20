x=[4,7,9,"abc"]
L=[x,[5]]

def Liste(l):
    for char in l:
        print(type(char))
        print(char)
        if type(char) == list:
            return Liste(char)
            
        
x=Liste(L)
        