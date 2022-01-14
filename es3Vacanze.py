#Scrivere un programma che data una lista ne stampi una sua
#permutazione casuale.

import itertools
import random

lista = [1,2,3,4]
permutazioni = list(itertools.permutations(lista))
x = random.randint(0,len(lista)+1)

print(x)
print(permutazioni)
print(permutazioni[x])

