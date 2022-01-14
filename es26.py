#3)Scrivi un programma in Python in cui chiedi all’utente un numero e comunichi se esso è primo oppure no. 
# Per stabilire se il numero è primo crea una funzione apposita che ritorni True se il numero è primo, False altrimenti. 


def primo(n):
    k = 2
    ok = True
    while(ok == True and k < n):
        if(n%k == 0):
            ok = False
        k = k + 1   
    return ok


n=int(input('Inserisci il numero intero:'))

if (primo(n) == True and n != 1):
    print(f"{n} è un numero primo")
else:
    print(f"{n} NON è un numero primo")
  
    
    
    


