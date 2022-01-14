#Scrivere un programma che data una lista qualsiasi la trasformi in un
#dizionario avente come chiavi gli indici della lista e come valori gli
#elementi.

lista = [0,1,"miao",3,4,5]
dizionario = {}

for k in range(len(lista)):
    dizionario[k] = lista[k]

print(dizionario)

#SOLUZIONE STILE PYTHON
for k, elemento in enumerate(lista):
    dizionario[k] = elemento
print(dizionario)

#DIZIONARIO COMPRIATION
dizionario={x: elemento for x,elemento in enumerate(lista)}
print(dizionario)