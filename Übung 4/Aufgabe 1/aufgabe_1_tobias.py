def anzahl(n):
    if n==0 :
        return 1
    else:
        m=0
        for iterator in range(n):
            m+=anzahl(iterator)-1       # T(iterator)-1 <=> T(i)-1
            m+=anzahl(n-(iterator+1))   # T(n-(iterator+1) <=> T(j)
            #                           # n-1 = i + j <=> n = (i-1) + j => T(n)=(T(i)-1) + T(j)
        return m
l=int(input("n"))

for i in range(l):     # Liefert die Moeglichen Kombinationen von j und i bei e=(A)B mit T(A) = i und T(B) = j
    #                  # Also bein n = 3: (0,2);(1,1);(2,0)
    print((i,l-(i+1)))

print(anzahl(l))   