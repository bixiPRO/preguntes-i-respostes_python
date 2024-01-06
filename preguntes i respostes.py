#PRE://Ha de mostrar una resposta aleatori i que l'usuari ha de respondre la pregunta
import random
#llista de preguntes amb la seva resposta
llista_preguntes=[("Quina es la capital de espana","Madrid"),("Quina es la capital de italia", "Roma")]

#bucle
resposta_bucle="si"
puntuacio=0
contador_vegadeswhile=0

while resposta_bucle == "si":
    contador_vegadeswhile+=1
    #numero aleatori
    seed = random.randint(0, 100)
    seed = (seed * 997) % 1000
    random_numero = (seed * 503) % 1000 / 100
    numero_pregunta = int(random_numero * (len(llista_preguntes)))

    #mostrar pregunta
    pregunta_elegir=llista_preguntes[numero_pregunta%len(llista_preguntes)]
    pregunta=pregunta_elegir[0]
    resposta=pregunta_elegir[1]
    resposta=resposta.strip()
    resposta=resposta.lower()
    print(pregunta)
    resposta_usuari=input("Resposta: ")
    resposta_usuari=resposta_usuari.strip()
    resposta_usuari=resposta_usuari.lower()
    if resposta_usuari==resposta:
        puntuacio+=1
        print("Resposta correcte! +1 punt")
    else:
        print("Resposta incorrecte!")
    #preguntar l'usuari si vol continuar jugant
    resposta_bucle=input("Vols continuar jugant? (si/no)")
    resposta_bucle=resposta_bucle.strip()
    resposta_bucle=resposta_bucle.lower()

print(f"Puntuació final: {puntuacio} / {contador_vegadeswhile}")
#POST://Mostra la puntuació de l'usuari d'acord de com ha respost la pregunta