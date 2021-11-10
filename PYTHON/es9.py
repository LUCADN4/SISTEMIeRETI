#Crea un programma in Python in cui assegni una parola a una variabile stringa e poi stampi le 
#lettere iniziali e finali della parola. 

stringa = "Luca corre"
print(stringa)
print(f"la lettera iniziale è {stringa[0]}")
print(f"la lettera finale è {stringa[-1]}")

#Crea un programma in Python in cui assegni una parola a una variabile stringa e poi stampi tutta la parola tranne le 
#lettere iniziali e finali della parola.

print(f"\n")
stringa = "Luca corre"
print(stringa)
print(stringa[1:9])

#Crea un programma in Python in cui assegni una parola a 
#una variabile stringa e poi stampi tutta la parola alternando una lettera si e una no.

print(f"\n")
stringa = "Luca corre"
print(stringa)
print(stringa[0:10:2])

#Crea un programma in Python in cui assegni una parola 
#a una variabile stringa e poi stampi la parola invertita. 

print(f"\n")
stringa = "Luca corre"
print(stringa)
print(stringa[::-1])

#Crea un programma in Python in cui assegni una parola di almeno 8 lettere a 
#una variabile stringa e poi stampi tutta la parola con un carattere ? al posto della terza lettera. 

print(f"\n")
stringa = "Luca corre"
print(stringa)

stringa_nuova = stringa[:2] + "?" +stringa[3:]
print(stringa_nuova)



