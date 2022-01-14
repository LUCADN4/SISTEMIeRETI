#3) Scrivi un programma in Python in cui chiedi all’utente un numero e comunichi se esso è divisibile per 2, oppure per 3, oppure per 5, oppure per nessuno di essi. 

def controllo(num,i):
    if(num%i == 0):
        ok = True
    else:
        ok = False
    return ok


num = int(input("Inserisci Numero: "))
esiste = False
for i in range(2,6):
    if(i != 4):
        if(controllo(num,i)):
            print(f"Numero divisibile per {i}")
            esiste = True
    
if (esiste == False):
    print(" Numero non divisibile per 2,3,5")

 

