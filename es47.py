"""[0,1,2,3,4]
^        ^
|        |
head      tail"""

#pass fa andare la funzione senza nulla all'interno
from cmath import pi


def enqueue(coda,elemento):
  pass#non fa  niente
  coda.append(elemento)
  
def dequeue(coda):
    if len(coda) != 0:
      return coda.pop(0)
    else:
      return None

"""coda = [0, 1, 2, 3, 4]

elemento = dequeue(coda)
while elemento != None:
    print(elemento)
    elemento = dequeue(coda)"""

cliente1 = {"nome":"Mario","id":123456}
cliente2 = {"nome":"Luigi","id":456789}
coda = []
enqueue(coda,cliente1)
enqueue(coda,cliente2)
print(coda)