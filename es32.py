#2) Creare una lambda function che ritorni True se una stringa inizia con lettera maiuscola, False altrimenti. 
c = input("Inserisci una stringa: ")

controllo = lambda c:(c[0]>='A' and c[0]<='Z')

if controllo(c) :
    print("La prima lettera è maiuscola")
else:
    print("La prima lettera NON è maiuscola")




