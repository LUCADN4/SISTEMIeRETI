#5) Genera una lista contenente i quadrati perfetti dispari minori di 1000.

import math

quadrati_perfetti = [k for k in range(1001) if math.sqrt(k)%1 == 0  if(k%2 != 0)]
print(quadrati_perfetti)
