#slicing 
stringa = "classe quarta A robotica"

print(f"Il primo carattere della stringa è {stringa[0]}")
print(f"l'ultimo carattere della stringa è {stringa[-1]}")

#prende i caratteri a partire da quello con indice 0 fino a aquellodi indice 6 ESCLUSO
print(stringa[0:6])

#dal 6 fino alla fine
print(stringa[6:])

#tutta la stringameno -2 caratteri
print(stringa[:-2])

#prende i caratteri da 2 a 13 saltando di due
print(stringa[2:14:2])

#tutta la stringa al contrario
print(stringa[::-1])

#stringa[15] = "B" #le stringhe in phyton sono IMMUTABILI
#TypeError: 'str' object does not support item assignment

stringa_nuova = stringa[0:14] + "B"+ stringa[15:]
print(stringa_nuova)
print(f"LA STRINGA MODIFICATA è:{stringa_nuova}")

print(print) #<built-in function print> stampa tutto 


