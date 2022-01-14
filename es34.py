#4) Data una lista di stringhe estrai da essa la lista di stringhe che sono palindrome e la lista di stringhe che hanno iniziale maiuscola. 
def palindromo(n):
    if str(n) == str(n)[::-1]:
        ok = True  
    else:
        ok = False
    return ok

def maiuscolo(n):
    return True if n[0].isupper() else False
    


y = ["Ciao","anna","oppo","Casa","anna"]
palindrome= []
maiuscole=[]

for n in y:
    if(palindromo(n)):
        palindrome.append(n)
    
    if(maiuscolo(n)):
        maiuscole.append(n)

print(palindrome)
print(maiuscole)