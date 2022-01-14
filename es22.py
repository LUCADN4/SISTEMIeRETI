print( "0 = somma 1 = sottrazione 2 = moltiplicazione 3 = divisione")
n = int(input("Inserisci operazione da svolgere: "))
dizionari = {0: "somma",1: "sottrazione" ,2:"moltiplicazione",3:"divisione"}

n1 = int(input("Inserisci il primo numero: "))
n2 = int(input("Inserisci il primo numero: "))



if n == 0:
    s = n1 +n2
elif n == 1:
    s = n2 - n1
elif n == 2:
    s = n1 * n2
elif n == 3:
    s = n1/n2
else:
    print("hai inserito il numero sbagliato")
   


print(f"la {dizionari[n]} è di {s}")

