#4) Scrivi un programma in Python che chieda all'utente un numero intero n e disegni, tramite turtle, il poligono regolare a n lati. 
import turtle

n = int(input("inserisci numero lati: "))
disegno = turtle.Turtle()
window = turtle.Screen()

for i in range(n):
    disegno.forward(50)
    disegno.left(360/n)
    
window.exitonclick()

