#6) Utilizza le list comprehension per generare la tavola pitagorica. 


quadrati = [x * y for x in range(1,11) for y in range(11)]

indice1 = 0
indice2 = 11


for k in range (10):
    print(quadrati[indice1:indice2])
    indice1 +=11
    indice2 +=11
    