#3)Scrivi un programma in Python che permetta all’utente di inserire le coordinate di due punti del piano cartesiano. 
# I punti devono essere salvati all’interno di tuple. Stampa la distanza euclidea tra i due punti. 

import math 

x1 = float(input("Inserisci x1: "))
y1 = float(input("Inserisci y1: "))

x2 = float(input("Inserisci x2: "))
y2 = float(input("Inserisci y2: "))

tupla = (x1,y1,x2,y2)

euclidea = math.sqrt((tupla[2] - tupla[0])**2 +(tupla[3] - tupla[1])**2)
print(euclidea)
