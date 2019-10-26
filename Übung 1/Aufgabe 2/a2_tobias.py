input_str=int(input("Geben Sie eine zweistellige Zahl ein:"))
x1=(input_str//10)%10
x2=input_str%10
#print(x1,x2)
print(str(x1+x2)*(x1+x2))