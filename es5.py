"""#assegnazione multipla
a, b = 4, 7 # un valore per ogni variabile
print(f"a vale {a} e b vale {b}")

a, b = b, a
print(f"a vale {a} e b vale {b}")"""

lista = ["A","E","I","O","U"]

parola = input("Inserisci la frase: ")
parola = parola.upper()

i = 0
nuova =""
ok = True
for k in parola:
    i = 0
    ok = True
    while(i  < 4 and ok == True): 
        if( k != lista[i]):
            nuova += k
            ok = False
        i = i +1
    
print(nuova)      
            
            

