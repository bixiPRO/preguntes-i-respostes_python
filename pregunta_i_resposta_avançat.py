#PRE: Mostra llista aleatoriament amb preguntes més d'una resposta
#Llista de preguntes i resposta
preguntes=[("Quin es el meu nom: ","Valtasar","Melhor","Raspar"),("Qui es el millor jugador de la lliga europeu","messi","ronaldo","yo")]

# buckle fins que l'usuari vol parar
while_si_no="si"
seed=int(input("Introdueix un numero aleatori: "))
#respostes de segun la pregunta
resposta1="Melhor"
resposta2="yo"
while while_si_no == "si":
    #mostrar preguntes aleatoris
    seed=(seed*997)%1000
    random=(seed*503)%1000/1000
    numero=int(random*(len(preguntes)))
    pregunta=preguntes[numero%len(preguntes)]
    #mostrar la pregunta
    pregunta_usuari=pregunta[0]
    A=pregunta[1]
    B=pregunta[2]
    C=pregunta[3]
    print(pregunta_usuari)
    seleccio_resposta=int(input(f"La solució és: \n1.{A}\n2.{B}\n3.{C}\n"))
    for i in range(0,3):
        

    

    while_si_no="no"


#POST: Mostra quants punts té, quantes preguntes ha contestat i d'aquest quantes ha fallat