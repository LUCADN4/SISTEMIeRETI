classi = ["4AROB","3AINF","2AROB","1BROB","4ACHI"]

indirizzi = {"ROB":"Smart-rob",
            "CHI": "Chimica", 
            "INF" : "Informatica"}

indice = 0

for classe in enumerate(classi):
    indice = indice + 1
    indirizzo = indirizzi[str(classe[-3:])]
    print(f"Posizione {indice} nella lista")
    print(f"la classe {classe} e dall'inidirizzo {indirizzo} ", end="\n\n")
