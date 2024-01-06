#PRE://Ha de mostrar una resposta aleatori i que l'usuari ha de respondre la pregunta
import random
#llista de preguntes amb la seva resposta
llista_preguntes=[("Quina es la capital de Algèria","Alger"), ("Quina es la capital de Kenya","Nairobi"), ("Quina es la capital de Sudan","Khartum"), ("Quina es la capital de Marroc","Rabat"), ("Quina es la capital de Gabon","Libreville"), ("Quina es la capital de Uruguai","Montevideo"), ("Quina es la capital de Perú","Lima"), ("Quina es la capital de Bolívia","Sucre"), ("Quina es la capital de Cuba","Habana"), ("Quina es la capital de Venezuela","Caracas"), ("Quina es la capital de Canadà","Ottawa"), ("Quina es la capital de Mèxic","Ciutat de Mexic"), ("Quina es la capital de Xina","Pequin"), ("Quina es la capital de Afganistan","Kabul"), ("Quina es la capital de Índia","Nova Delhi"), ("Quina es la capital de Japó","Toquio"), ("Quina es la capital de Espanya","Madrid"), ("Quina es la capital de França","Paris"), ("Quina es la capital de Romania","Bucarest"), ("Quina es la capital de Liechtenstein","Vaduz"), ("Quina es la capital de Bielorússia","Minsk"), ("Quina es la capital de Itàlia","Roma"), ("Quina es la capital de Dinamarca","Copenhaguen"), ("Quina es la capital de Austràlia","Canberra")]

#bucle
resposta_bucle="si"
puntuacio=0
contador_vegadeswhile=0

print("IMPORTANT:")
print("- La resposta ha de ser en Català")
print("- No posis exentos en ninguna resposta, sinó declarara com a malament")

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

    if resposta_bucle != "no":
            resposta_bucle="si"

print(f"Puntuació final: {puntuacio} / {contador_vegadeswhile}")
#POST://Mostra la puntuació de l'usuari d'acord de com ha respost la pregunta