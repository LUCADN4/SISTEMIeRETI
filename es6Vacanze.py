#Il file covid-19_gen1.txt contiene la sequenza genomica RNA di un
#virus SARS-COV-2. L&#39;RNA è una sequenza in cui si alternano 4
#simboli (detti nucleotidi): A, T, C, G. L&#39;RNA del virus SARS-COV-2
#contiene 29903 nucleotidi. Leggi covid-19_gen1.txt il file e crea un
#dizionario Python avente come chiavi i nucleotidi A, T, C, G e come
#valori i rispettivi conteggi.

def main():
    f = open("./covid-19_gen1.txt","r")
    dizionario = {}
    righe =f.readlines()
    a,t,c,g=0,0,0,0

    for riga in righe:
        for k in range(71):
            if riga[k:k+1] == 'A':
                a+=1
            elif riga[k:k+1] == 'T':
                t+=1
            elif riga[k:k+1] == 'C':
                c+=1
            elif riga[k:k+1] == 'G':
                g+=1

    dizionario['A'] = a
    dizionario['T'] = t
    dizionario['C'] = c
    dizionario['G'] = g

    print(dizionario)
    f.close()

if __name__ == "__main__":
    main()
