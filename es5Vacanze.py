#Scrivere un programma in Python che prenda in input il nome file di
#un programma scritto in C. Il programma deve leggere il file e:
#1. Contare il numero di righe totali
#2. Contare il numero di chiamate alla funzione “printf”
#3. Contare il numero di linee di commento.

f = open("fileC.txt","r")
c,s=0,0
#1. Contare il numero di righe totali
righe = f.readlines()
#print(righe)
print(f"Numero di righe del file: {len(righe)}")

for riga in righe:
    if "printf" in riga:#riga[0:6] == "printf"
        c+=1
    elif "//" in riga: #riga[0:2] == "//"
        s+=1
#2. Contare il numero di chiamate alla funzione “printf”
print(f"Numero di prinf presenti: {c}")
#3. Contare il numero di linee di commento.
print(f"Numero di commenti presenti: {s}")

f.close()



