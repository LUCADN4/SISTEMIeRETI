#4)Calcola, mediante un opportuno programma in Python, quanti sono i numeri primi minori di 1000. 
# Per stabilire se il numero è primo crea una funzione apposita che ritorni True se il numero è primo, False altrimenti. 

def primo(n):
    k = 2
    ok = True
    while(ok == True and k < n):
        if(n%k == 0):
            ok = False
        k = k + 1   
    return ok



lista,c,s=[],0,0

for i in range(1001):
    c = c + 1
    lista.append(c)

    if (primo(c) == True and c != 1):
        print(f"{c} è un numero primo")
        s = s + 1
    else:
        print(f"{c} NON è un numero primo")
    
print(f"I numeri primi da 0 a 1000 sono: {s} ")

   