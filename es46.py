"""def push(pila,elemento):
    pila.append(elemento)

def pop(pila):
    if(len(pila) != 0):
        return pila.pop()
    else:
        return None
        


pila = []
push(pila,9999)
print(pila)
pop(pila)
print(pila)"""

def push(pila,elemento):
    pila.append(elemento)

def pop(pila):
    if len(pila) != 0:
        return pila.pop()
    else:
        return None

pila = ['a','e','i','o','u']

elemento = pop(pila)
while elemento != None:
    print(elemento)
    elemento = pop(pila)
