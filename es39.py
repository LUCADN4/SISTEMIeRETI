
f = open("./elencoNumPrimi.txt","w")

def primo(n):
    k = 2
    ok = True
    while(ok == True and k < n):
        if(n%k == 0):
            ok = False
        k = k + 1   
    return ok

lista=[]
n = 2
c = 0

while(c < 100):
    if (primo(n) == True):
        f.write( str(n) + "\n")
        c = c + 1
    n = n + 1    
    
    

    
f.close()