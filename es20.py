voto = int(input("Inserisci il voto: "))
if voto >= 8:
    print("eccellente")
elif voto >= 7 & voto < 8:
    print("Buono")
elif voto >= 6 & voto < 7:
        print("Sufficente")
else:
    print("Insufficente")

while (voto < 6):
    print("Sei insufficente")
    voto = int(input("Inserisci il voto: "))