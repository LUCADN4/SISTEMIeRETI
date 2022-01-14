alfabeto = ["A" , "B" , "C" , "D" , "E" , "F" , "G" , "H" , "I" , "J" , "K" , "L" , "M" , "N" , "O" , "P" , "Q" , "R" , "S" , "T" , "U" , "V" , "W" , "X" , "Y" , "Z", " "]


def cifrario(frase,chiave,numero):
    nuova_parola = ""
    for k in frase:
        ok = True
        i = 0
        while(i < 27 and ok == True):
            if( alfabeto[i] == k):
                ok = False  
                nuova_parola += alfabeto[(i+(chiave)*numero)%27]                        
            i+=1
    return nuova_parola

def main():
    
    comando = int(input("Codifica[0] o Decodifica[1]: "))
    parola = input("Inserisci la Parola: ")
    numero = int(input("Numero di spostamenti: "))
    parola = parola.upper()
    print(parola)
    if (comando == 0):
        chiave = 1
        nuova_parola = cifrario(parola,chiave,numero) 
        print(f"parola Codificata =  {nuova_parola}")
    else:
        chiave = -1
        nuova_parola = cifrario(parola,chiave,numero) 
        print(f"parola Decodificata = {nuova_parola}")

if __name__ == "__main__":
    main()