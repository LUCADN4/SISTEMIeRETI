# crea  un programma in Python in cui inizializzi la lista x = [0,1,2,3,5,6,7,8] e poi
#creare due nuove liste conteneti ciascuna una delle due metà della lista
#aggiungi il valore 5 alla lista contenente la prima metà

#a//b divisione interi         a/b divisione per float                  a**b eleva a potenza        a%b è il MOD
x = [0,1,2,3,5,6,7,8]

prima_parte = x[:4]
print(prima_parte)
seconda_parte = x[4:]
print(seconda_parte)

prima_parte.append(5)
print(prima_parte)