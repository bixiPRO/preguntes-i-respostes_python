#Ha de mostrar una resposta aleatori i que l'usuari ha de respondre la pregunta
#llista de preguntes amb la seva resposta
llista_preguntes=[("Quina es la capital de espana","Madrid"),("Quina es la capital de italia", "Roma")]

#numero aleatori
seed=48
seed = (seed * 997) % 1000
random = (seed * 503) % 1000 / 100
numero_pregunta = int(random * (len(llista_preguntes)))

print(numero_pregunta)
                                
for i in llista_preguntes:
    print(i)
#Mostra la puntuació de l'usuari d'acord de com ha respost la preguntagit