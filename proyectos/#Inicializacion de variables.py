#Inicializacion de variables
vidas = 3
puntos = 0
#---Pregunta 1---
respuesta_1 = input("¿Cuanto es 8 x 5?")
if int(respuesta_1) == 40:
    print("¡CORRECTO!")
    puntos += 10
    print("(Sonido: pop)")
else:
    print("¡INCORRECTO!")
    vidas -= 1
    print("(Sonido: pop)")
#---Pregunta 2---
respuesta_2 = input("¿Qué número falta en la serie: 5, 10, 15, ..., 25?")
if int(respuesta_2) == 20:
    print("¡CORRECTO!")
    puntos += 10
    print("(Sonido: pop)")
else:
    print("¡INCORRECTO!")
    vidas -= 1
    print("(Sonido: pop)")
#---Pregunta 3---
respuesta_3 = input("Un gato tiene 4 patas. ¿Cuántas patas tienen 3 gatos?")
if int(respuesta_3) == 12:
    print("¡CORRECTO!")
    puntos += 10
    print("(Sonido: pop)")
else:
    print("¡INCORRECTO!")
    vidas -= 1
    print("(Sonido: pop)")
#---Condicion final---
if vidas <= 0:
    print("GAME OVER")
else:
    print("¡GANASTE!")