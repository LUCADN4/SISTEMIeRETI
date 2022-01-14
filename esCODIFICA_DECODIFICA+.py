alfabeto = ["A" , "B" , "C" , "D" , "E" , "F" , "G" , "H" , "I" , "J" , "K" , "L" , "M" , "N" , "O" , "P" , "Q" , "R" , "S" , "T" , "U" , "V" , "W" , "X" , "Y" , "Z", " "]


comando = int(input("Codifica[0] o Decodifica[1]: "))
parola = input("Inserisci la Parola: ")
lista= []
parola = parola.upper()
print(parola)
n  = 0

if (comando == 0):
    nuova_parola = ""
    for k in range(len(parola)):
        i = 0
        while(i < 27):   
            nuova_parola = alfabeto[i] 
            lista.append(nuova_parola)
            nuova_parola = ""                        
            i+=1
    print(f"LISTA Codificata =  {lista}")
