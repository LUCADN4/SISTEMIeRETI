#2) Utilizzando il modulo random (https://docs.python.org/3/library/random.html), simula dieci lanci di un dado per Alice e dieci lanci di un dado per Bob, 
# mediante list comprehension. Il dado è a sei facce. Salva i lanci all’interno di un file, su dieci righe, 
# in cui la prima colonna corrisponde ai lanci di Alice e la seconda a quelli di Bob. Utilizza la virgole come separatore all’interno delle righe. 

import random

f = open("./NumeriRandom.txt","w")

ALICE = [random.randint(1,6) for i in range(10) ]
BOB = [random.randint(1,6) for i in range(10) ]

for i in range(10):
    f.write(str(ALICE[i]) + " , " + str(BOB[i]) + "\n")


f.close()