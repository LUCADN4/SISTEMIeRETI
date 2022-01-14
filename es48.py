class Pila():
    #costruttore
    def __init__(self,lista):
        self.pila= lista

p1 = Pila([1,2,3])#richiama il costruttore ma il self non si vede
print(p1.pila)