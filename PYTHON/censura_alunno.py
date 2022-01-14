"""
segreteria di una scuola, inserisce cognome di alunno e voto di condotta per tutti gli alunni.
Vengono salavati su file con cognome, voto però per privacy cgonme solo prima lettera seguita da  *
""" 
def controllo():
    k = False
    while(k == False):
        x = int(input("Voto condotta: "))
        if(x >= 0):
            k = True
    return x

def controllo_Alunni():
    k = False
    while(k == False):
        x = int(input("Inserisci numero si alunni: "))
        if(x >= 0):
            k = True
    return x

def main():
    f = open("./Elenco_Condotta.txt","w")
    numero = controllo_Alunni()
    i = 0

    while(i < numero):
        alunno = input(f"Inserisci nome alunno {i}: ")
        voto = controllo()
        x = len(alunno)-1
        #f.write( (alunno[0] + x * "*") + ","+str(voto) +("\n"))
        f.write(f"{alunno[0] + x * '*'}, {voto}\n")
        i+=1

    f.close()

if __name__ == "__main__":
    main()