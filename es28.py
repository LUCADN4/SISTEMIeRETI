#list comprehension
def primo(n):
    k = 2
    ok = True
    while(ok == True and k < n):
        if(n%k == 0):
            ok = False
        k = k + 1   
    return ok



primi = [k for k in range(2,1003) if primo(k)]
# k = conteggio
#print(primi)

num = [k for k in range(1000) if(k%2 != 0)]
#print(num)

nomi = ["marco", "paolo", "marta", "sara"]

nomi_m = [nome for nome in nomi if (nome[0] == "m")]
print(nomi_m)
    
