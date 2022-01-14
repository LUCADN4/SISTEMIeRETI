#1) Utilizzando le list comprehension scrivi un programma che crei una lista con tutte le potenze di due minori o uguali a un valore inserito dall’utente. Stampa la lista. 

due= 2
num = int(input("Inserisci numero: "))

potenze = [due**i for i in range(num) if(due**i  <= num)]
    
print(potenze)
    
    
