#3)Scrivi un programma Python che chieda all’utente i suoi dati anagrafici (nome, cognome, data di nascita), li salvi all’interno di un dizionario e
#  infine salvi il dizionario su un file, elemento per elemento. 
f = open("./elencoDizionario.txt","w")
dizionario,i={},0
n = int(input("Numero di persone presenti: "))

while i < n:
    nome = input("Inserisci nome:")  
    cognome = input("Inserisci cognome:") 
    g = int(input("Inserisci giorno: "))
    mese = int(input("Inserisci mese: ")) 
    anno = int(input("Inserisci anno: "))
    dizionario[i]= nome + " " +cognome + " "+ str(g) + "/" + str(mese)+ "/" + str(anno)
    f.write(str(dizionario[i])+ "\n")

    i = i + 1

f.close()