import random
#Ha de mostrar una resposta aleatori i que l'usuari ha de respondre la pregunta
#llista de preguntes amb la seva resposta
llista_preguntes=[("Quina es la capital de espana","Madrid"),("Quina es la capital de italia", "Roma")]

#numero aleatori
seed= random.randint(0,100)
seed = (seed * 997) % 1000
random = (seed * 503) % 1000 / 100
numero_pregunta = int(random * (len(llista_preguntes)))

#mostrar pregunta
pregunta_elegir=llista_preguntes[numero_pregunta%len(llista_preguntes)]
pregunta=pregunta_elegir[0]
#bucle
resposta="si"
puntuació=0
while resposta == "si":
    print(pregunta)

#Mostra la puntuació de l'usuari d'acord de com ha respost la pregunta