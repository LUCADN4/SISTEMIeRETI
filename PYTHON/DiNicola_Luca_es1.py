import random

def movimento():
    c=False
    while(c==False):
        num = random.randint(-1,1)
        if num != 0:
            c=True
    return num
   
t = 60*60*24*5

spostamenti = [movimento() for _ in range(t)]
s = 0

for i in range(t):
    s += spostamenti[i]

print(f"Spostamento : {s} ")