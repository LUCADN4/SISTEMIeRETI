#1) Cercare la documentazione del modulo turtle e scrivere una breve relazione sulle funzioni che contiene e sul suo utilizzo. 
"""Turtle è una funzionalità di Python che ci permette di disegnare. 
tartaruga è una libreria Python preinstallata che consente agli utenti di creare immagini e forme con una tela virtuale fornita. 
La penna su schermo che usi per disegnare si chiama tartaruga."""

import turtle

snow = turtle.Turtle()
turtle.Screen().bgcolor("blue")
snow.color("white")
window = turtle.Screen()

f = open("./istruzioni.txt","w")

for i in range(8):
  snow.forward(40)#
  f.write("forward:" + str(40) + "\n")
  snow.backward(40)
  f.write("backward:" + str(40) + "\n")
  snow.forward(60)#
  f.write("forward:" + str(60) + "\n")
  snow.right(-45)
  f.write("right:" + str(-45) + "\n")
  snow.forward(40)
  f.write("forward:" + str(40) + "\n")
  snow.backward(40)
  f.write("backward:" + str(40) + "\n")
  snow.right(90)#
  f.write("right:" + str(90) + "\n")
  snow.forward(40)
  f.write("forward:" + str(40) + "\n")
  snow.backward(40)
  f.write("backward:" + str(40) + "\n")
  snow.right(-45)#
  f.write("right:" + str(-45) + "\n")
  snow.forward(60)
  f.write("forward:" + str(60) + "\n")
  snow.right(-45)#
  f.write("right:" + str(-45) + "\n")
  snow.forward(40)
  f.write("forward:" + str(40) + "\n")
  snow.backward(40)
  f.write("backward:" + str(40) + "\n")
  snow.right(90)#
  f.write("right:" + str(90) + "\n")
  snow.forward(40)
  f.write("forward:" + str(40) + "\n")
  snow.backward(40)
  f.write("backward:" + str(40) + "\n")
  snow.right(-45)
  f.write("right:" + str(-45) + "\n")
  snow.forward(40)
  f.write("forward:" + str(40) + "\n")
  snow.backward(160)#
  f.write("backward:" + str(160) + "\n")
  snow.right(45)#
  f.write("right:" + str(45) + "\n")

f.close()
window.exitonclick()#mettere sempre









