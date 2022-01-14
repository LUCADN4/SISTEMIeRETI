# le liste sono mutanbili

#lista = [3,3.1415,"ciao"]                                  #lista etereogenea
#print(lista)

#print(lista[1:-1])                                         #indicizazione con le stesse regole delle stringhe

#lista[1] = 2.645
#print(lista)

numeri_primi = [2,3,5,7,11,13]
numeri_primi.append(17)
print(numeri_primi)
print(f"la lunghezza è: {len(numeri_primi)} ")

#altri_numeri_primi = [19,23,29]
#molti_numeri_primi = numeri_primi + altri_numeri_primi                         # liste concatenate
#print(molti_numeri_primi)

#print(5*altri_numeri_primi)                                                # stampa tutta la lista per 5 volte


for numero_primo in numeri_primi: # il : impostante alla fines
    print(numero_primo,end="-")    # end non va a capo
