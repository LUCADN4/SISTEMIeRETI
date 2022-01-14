#Il file prezzi.csv (separatore ;) contiene le serie storiche mensili dei
#prezzi di alcuni generi alimentari dal Settembre 2011 a Dicembre
#2016. Immagina una spesa costituita da 5 generi alimentari a tua
#scelta e crea una lista contenente la serie storica del prezzo della tua
#spesa ottenuta sommando i prezzi dei generi alimentari scelti.
#Calcola mese / anno in cui la tua spesa ha costi minimi e massimi.
import csv

def controllo(m):# controllo dei numero massimo di prodotti e che non venga inserito numero negativo
    if(m >= 0 and m <= 29):
        ok = True
    else:
        ok = False
    return ok

def annoTrova(x): #per definire anno con spesa massima e minima
    if(x == 0):
        anno="2011"
    elif(x == 1):
        anno="2012"
    elif(x == 2):
        anno="2013"
    elif(x == 3):
        anno="2014"
    elif(x == 4):
        anno="2015"
    elif(x == 5):
        anno="2016"
    return anno

lista,d,i,serieStorica= [],{},1,[]   #lista contiene tutto il file #serieStorica per contenere il prodotto selezionato
spesaMeseAnno=[] #somma della spesa per ogni mese per ogni anno

with open("prezzi.csv", "r") as file:
    righe = csv.reader(file, delimiter=";")#
    for riga in righe:
        lista.append(riga)
    f4=lista[0][2:]#contiene nomi prodotti TOLGO anno e mese
    for k in range(len(f4)):
        d[k]=f4[k]

    for k in range(len(f4)):
         print(f"Prodotto:{k} è {d[k]}")
   
    print("\n")
    while(i < 6): #prodotto 
        m = int(input(f"inserisci {i} alimento da prendere: "))
        if(controllo(m)):
            serieStorica.append(m)
            i+=1
#print(serieStorica)   

#serve per sommare tutti i prodotti con la variazione durante il mese 
s = 0
for k in range(59):
    s = 0
    for i in range(5):
        s = s+float( lista[k+1][serieStorica[i]+2])
    spesaMeseAnno.append(lista[k+1][0])
    spesaMeseAnno.append(lista[k+1][1])
    spesaMeseAnno.append(s)
    print(f"Spesa del {lista[k+1][0]} nel mese di {lista[k+1][1]} è di {s}")

#print(spesaMeseAnno) #calcola il maggiore e minore nella lista spesaMeseAnno
max =spesaMeseAnno[2]
min =spesaMeseAnno[2]
meseMax="Settembre"
meseMin="Settembre"
due = 2

while (due < len(spesaMeseAnno)-1):
    if(float(spesaMeseAnno[due+3]) > (max)):
        meseMax=spesaMeseAnno[due+2]
        max=spesaMeseAnno[due+3]
    if(float(spesaMeseAnno[due+3]) < (min)):
        meseMin=spesaMeseAnno[due+2]
        min=spesaMeseAnno[due+3]
    due = due+3

print(f"Il mese con la spesa Maggiore nel mese di {meseMax} con una spesa di {max}")
print(f"Il mese con la spesa Minore nel mese di {meseMin} con una spesa di {min}")
print("\n")

maxMinAnno=[]
sA1,sA2,sA3,sA4,sA5,sA6=0,0,0,0,0,0
due = 2
for k in range(len(spesaMeseAnno)):
    if(spesaMeseAnno[k]=="2011"):
        sA1=sA1+(spesaMeseAnno[due])
        due = due+3
    if(spesaMeseAnno[k]=="2012"):
        sA2=sA2+(spesaMeseAnno[due])
        due = due+3
    if(spesaMeseAnno[k]=="2013"):
        sA3=sA3+(spesaMeseAnno[due])
        due = due+3
    if(spesaMeseAnno[k]=="2014"):
        sA4=sA4+(spesaMeseAnno[due])
        due = due+3
    if(spesaMeseAnno[k]=="2015"):
        sA5=sA5+(spesaMeseAnno[due])
        due = due+3
    if(spesaMeseAnno[k]=="2016"):
        sA6=sA6+(spesaMeseAnno[due])
        due = due+3

maxMinAnno.append(sA1)
maxMinAnno.append(sA2)
maxMinAnno.append(sA3)
maxMinAnno.append(sA4)
maxMinAnno.append(sA5)
maxMinAnno.append(sA6)

#print(maxMinAnno)
i=0 
k=0 #se la prima spesa è la piu grande
j=0 # se la prima spesa è la piu piccola
maxDIM = maxMinAnno[0]
minDIM = maxMinAnno[0]
for i in range(6):
    if(maxMinAnno[i] > maxDIM):
        k=i
        maxDIM=maxMinAnno[i]
    if(maxMinAnno[i] < minDIM):
        j=i
        minDIM=maxMinAnno[i]
    i+=1

anno= annoTrova(k)
print(f"l' anno {anno} ha avuto una spesa massima di {maxDIM}")
anno= annoTrova(j)
print(f"l' anno {anno} ha avuto una spesa minima di {minDIM}")


       

