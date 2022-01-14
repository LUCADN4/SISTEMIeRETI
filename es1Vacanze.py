#Scrivere un programma che data una lista qualsiasi ne elimini i duplicati.

lista = [2, 6, 6, 6, 6, 8]
lista2 = []

for k in lista:
    if k not in lista2: #elemento in lista ritorna un bool 
        lista2.append(k)
 
print(lista2)
