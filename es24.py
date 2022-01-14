#1)Crea un programma Python che permetta all'utente di inserire un numero qualunque di interi all'interno di una lista. 
# Stampa la lista al termine dell'inserimento.

n=int(input('Inserisci il numero di elementi:'))
lista,c=[], 0

for i in range(n):
    c = int(input("Inserisci numero intero:"))
    lista.append(c)
    
print(lista)   
    

