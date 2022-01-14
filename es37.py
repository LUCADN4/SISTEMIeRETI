#7) Utilizza il modulo random per simulare una partita a dadi tra Alice e Bob.
import random

alice = random.randint(1,6)

bob = random.randint(1,6)



if alice > bob: 
    print(f"Vince alice con:{alice}") 
else: 
    print(f"Vince bob con:{bob}")