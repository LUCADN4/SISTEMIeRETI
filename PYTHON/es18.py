#4)Scrivi un programma in Python che permetta all’utente di inserire due numeri qualsiasi. 
# Crea una lista contenente: 
# la somma dei quadrati dei due numeri 
# Il quadrato della somma dei numeri 
# la differenza tra i  quadrati dei due numeri 
# la differenza tra i numeri al quadrato 
# Stampa la lista ottenuta.

n1 = float(input("Inserisci n1: "))

n2 = float(input("Inserisci n2: "))

x =[]
x.append(n1**2 + n2**2)
x.append((n1+n2)**2)
x.append(n1**2 - n2**2)
x.append((n1-n2)**2)
print(x)
