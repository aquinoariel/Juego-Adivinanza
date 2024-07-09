# Estructuras de control condicionales

#if, elif, else


#visa = True
#pasaporte = False
#
#if visa:
#    print("Estas habilitado para viajar a EEUU")
#elif pasaporte and not visa:
#    print("No podes viajar a EEUU, pero si a Europa")
#else:
#    print("No podes salir del pais")


import random


numero_secreto = random.randint(0,101)
cantidad_intentos = 0
cantidad_intentosMax = 5
adivinado = False

print("Bienvendio a la adivinanza")

while not adivinado and cantidad_intentos < cantidad_intentosMax:
    entrada = int(input("Selecciona un numero: "))
    if entrada == numero_secreto:
        print("Felicitaciones ganaste!")
        break
    elif entrada < numero_secreto:
        print ("El numero que ingresaste es menor")
    else:
        print("El numero que ingresaste es mayor")
    cantidad_intentos += 1
    
if cantidad_intentosMax:
        print("Game Over llegaste a la cantidad maxima de intentos")