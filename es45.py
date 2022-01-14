#5) Scrivi un programma in Python che chieda all'utente un numero intero n. Il programma deve creare una lista contente due diverse turtle,
#  orientate in direzioni opposte. Ciascuna turtle disegna poi il poligono regolare a n lati.

import turtle

n = int(input("inserisci numero lati: "))
disegno1 = turtle.Turtle()
disegno2 = turtle.Turtle()
lista = [disegno1,disegno2]
window = turtle.Screen()

lista[1].right(180)

for _ in range(n):
    for i in range(2):
        lista[i].forward(50)
        lista[i].left(360/n)
    
    
window.exitonclick()