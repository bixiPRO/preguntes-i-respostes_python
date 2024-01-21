#PRE//repartir cartes
cartas =["QS","6C","5H","JS","7S","3C","5D","AH","10S","JC","4C","3H","7C","QH","7H","2H","8C","8H","9H","10D","10C","2D","9C","KD","4S","AD","6H","6D","2C","AS","AC","10H","QC","KS","KC","8D","4D","8S","5C","3S","4H","QD","7D","9S","3D","2S","6S","JD","5S","JH","9D","KH"]
#jugadors
jugador1=[]
jugador2=[]
jugador3=[]
jugador4=[]
cartes_aleatories=[]


#Que cada jugador tinguin 13 cartes random
seed=int(input("Introdueix un numero aleatori: "))
#Hacer una lista de cartas_aleatorias donde estan las cartas en aleatorio
for i in cartas:
    seed = (seed * 997) % 1000
    random = (seed * 503) % 1000 / 1000
    numero_pregunta = int(random *(len(cartas)))
    numero_carta=cartas[numero_pregunta%len(cartas)]
    cartes_aleatories.append(numero_carta)

#repartir 13 cartes jugador1
contador=0
for j in cartes_aleatories:
    if contador!=13:
        jugador1.append(j)
        contador+=1

for g in jugador1:
    cartes_aleatories.remove(g)


#repartir 13 cartes jugador2
contador=0
for j in cartes_aleatories:
    if contador!=13:
        jugador2.append(j)
        contador+=1

for g in jugador2:
    cartes_aleatories.remove(g)


#repartir 13 cartes jugador3
contador=0
for j in cartes_aleatories:
    if contador!=13:
        jugador3.append(j)
        contador+=1

for g in jugador3:
    cartes_aleatories.remove(g)


#repartir 13 cartes jugador4
contador=0
for j in cartes_aleatories:
    if contador!=13:
        jugador4.append(j)
        contador+=1

for g in jugador4:
    cartes_aleatories.remove(g)



print(cartes_aleatories)
print("")
print(jugador1)
print("")
print(jugador2)
print("")
print(jugador3)
print("")
print(jugador4)
 
#POST//determinar qui ha guanyat