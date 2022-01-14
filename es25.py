#2)Crea una funzione Python che data una lista di numeri, 
# ritorni il suo valore massimo e il suo valore minimo. 

def mag(lista):
    min = lista[0]  
    max = lista[0]
    for i in range(n):
        if(lista[i] < min):
            min = lista[i]

        if(lista[i] > max):
            max = lista[i]
    return min,max


n=int(input('Inserisci il numero di elementi:'))
lista,c=[],0

for i in range(n):
    c = int(input("Inserisci numero intero:"))
    lista.append(c)

min,max = mag(lista)

print(f"Minimo: {min}, Massimo: {max}")

#print(f"Il numero massimo è:{(max(lista))}")
#print(f"Il numero massimo è:{(min(lista))}")

