#lambda function
def somma_moltiplicazione(x,y):
    somma = x + y
    molti = x * y
    return somma,molti

a,b = 10,4

s, m = somma_moltiplicazione(a,b)
print(s,m)

somma_moltiplicazione2 = lambda x,y: (x+y,x*y)

"""

def somma_moltiplicazione(x,y):
    somma = x + y
    molti = x * y
    return {"somma": somma,"molti": molti}

a,b = 10,4

print(somma_moltiplicazione(a,b))

"""
