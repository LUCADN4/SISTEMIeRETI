import turtle

snow = turtle.Turtle() 
finestra = turtle.Screen() 


f = open("./istruzioni.txt","r")
righe = f.readlines()
#print(righe)

for riga in righe:
    lista = riga.split(":")
    #forward:100
    #["forward","100\n"]
    #valore = comando[1]
    if(lista[0]=="forward"):
        snow.forward(int(lista[1][:-1]))
    elif(lista[0]=="right"):
        snow.right(int(lista[1][:-1]))
    elif(lista[0]=="backward"):
        snow.backward(int(lista[1][:-1]))#elimina -1 unltino carattere \n
    elif(lista[0]=="left"):
        snow.left(int(lista[1][:-1]))
    else:
        print("COMANDO NON TROVATO")
      

finestra.exitonclick()
f.close()

#print(len(righe))