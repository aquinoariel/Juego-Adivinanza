
nombre1 = input("Como se llama el jugador 1? ")
nombre2 = input("Como se llama el jugador 2? ")

puntaje_jugador1 = 0
puntaje_jugador2 = 0

veces_jugadas = 0
juegos_maximos = 3

while veces_jugadas < juegos_maximos:
     jugador1 = input("Hola {}, piedra, papel o tijeras? ".format(nombre1)).lower()
     jugador2 = input("Hola {}, piedra, papel o tijeras? ".format(nombre2)).lower()
     veces_jugadas += 1

     condicion1 = jugador1 == "piedra" and jugador2 == "tijeras"
     condicion2 = jugador1 == "papel" and jugador2 == "piedra"
     condicion3 = jugador1 == "tijeras" and jugador2 == "papel"
     
     if jugador1 == jugador2:
        print ("Empataron")
     elif condicion1 or condicion2 or condicion3:
        print ("Gana {}".format(nombre1))
        puntaje_jugador1 += 1
     else:
        print("Gana {}".format(nombre2))
        puntaje_jugador2 += 1

ganador1 = puntaje_jugador1 > puntaje_jugador2
ganador2 = puntaje_jugador1 < puntaje_jugador2

if veces_jugadas == juegos_maximos:
   if ganador1:
      print ("El juego lo gana {}".format(nombre1))
   elif ganador2:
       print ("El juego lo gana {}".format(nombre2))
   else:
       print ("El juego termino en empate")
            

      
