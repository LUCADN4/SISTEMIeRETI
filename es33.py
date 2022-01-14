#3) Creare una lambda function che ritorni True se una stringa è palindroma, False altrimenti. 

y = ("anna")
controllo = lambda stringa:(stringa == stringa[::-1])

if  (controllo(y)):
    print("Palindroma")
else:
    print("NON è Palindroma")


