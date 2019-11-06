s=input("Geben sie bitte was ein, damit ich es in Kleinbuchstaben wiederholen darf^^ ").lower()
v=str(input("Geben sie bitte einen Vocal ein "))
for char in s: 
    if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
        charindex = s.index(char)
        s=s[0:charindex] + v + s[charindex+1:]
print(s)
            
    
    




