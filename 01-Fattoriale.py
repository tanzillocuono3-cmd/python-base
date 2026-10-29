a=int(input("Inserire numero:"))
if a==0:
    print("Fattoriale è 1")
else:
    fattoriale=1
    for i in range (1,a+1):
        fattoriale=fattoriale*i
    print("Fattoriale è ",fattoriale)    
