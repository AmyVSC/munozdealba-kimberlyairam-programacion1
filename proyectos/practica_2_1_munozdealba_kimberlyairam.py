print("Ejercicios clase 28/09 Unidad 2")
# Ejercicio 1 Datos personales
print("--- Ejercicio 1 ---")
#entrada 1 
print("- Entrada 1-")
nombre = "Airam"
edad = "18"
ciudad = "Guadalajara"
print(nombre, edad, ciudad)
#entrada 2 
print("- Entrada 2-")
nombre = "Yamir"
edad = "19"
ciudad = "Guadalajara"
print(nombre, edad, ciudad)
# Ejercicio 2 Actualizar un contador
print("--- Ejercicio 2 ---")
#entrada 1 
print("- Entrada 1-")
contador1 = 0 
contador1 = contador1 + 1
print("Contador:", contador1)
contador1 = contador1 + 1
print("Contador:", contador1)
contador1 = contador1 + 1
print("Contador:", contador1)
#entrada 2
print("- Entrada 2-")
contador2 = 64
contador2 = contador2 + 1
print("Contador:", contador2)
contador2 = contador2 + 1
print("Contador:", contador2)
contador2 = contador2 + 1
print("Contador:", contador2)
# Ejercicio 3 Constante de conversion
print("--- Ejercicio 3 ---")
PULGADAS_A_CM = 2.54
#entrada 1 
print("- Entrada 1-")
pulgadas1 = 10
centimetros = pulgadas1 * PULGADAS_A_CM
print("Centimetros:", centimetros)
#entrada 2
print("- Entrada 2-")
pulgadas2 = 26.38
centimetros = pulgadas2 * PULGADAS_A_CM
print("Centimetros:", centimetros)
# Ejercicio 4 Area de un rectangulo
print("--- Ejercicio 4 ---")
#entrada 1
print("- Entrada 1-")
base1 = 2
altura1 = 33.5
area1 = base1 * altura1
perimetro1 = 2 * (base1 + altura1)
print("El area del rectangulo es:", area1)
print("El perimetro del rectangulo es:", perimetro1)
#entrada 2 
print("- Entrada 2-")
base2 = 4
altura2 = 16.75
area2 = base2 * altura2
perimetro2 = 2 * (base2 + altura2)
print("El area del rectangulo es:", area2)
print("El perimetro del rectangulo es:", perimetro2)
# Ejercicio 5 Total con IVA
print("--- Ejercicio 5 ---")
IVA = 0.16
#entrada 1 
print("- Entrada 1-")
precio1 = 67
precio1 = precio1 + (precio1 * IVA)
print("Precio con IVA:", precio1)
#entrada 2 
print("- Entrada 2-")
precio2 = 57.77
precio2 = precio2 + (precio2 * IVA)
print("Precio con IVA:", precio2)
# Ejercicio 6 Intercambio de valores
print("--- Ejercicio 6 ---")
#entrada 1
print("- Entrada 1-")
A = 67
B = 69
print("Antes: A=", A, "y", B)
xd = A
A = B
B = xd
print("Despues: A=", A, "y", B)
#entrada 2
print("- Entrada 2-")
a2 = 99
b2 = 1
print("Antes: a =", a2, "b =", b2)
temp2 = a2
a2 = b2
b2 = temp2
print("Después: a =", a2, "b =", b2)
# Ejercicio 7  Identificar tipos con type()
print("--- Ejercicio 7 ---")
#entrada 1
print("- Entrada 1-")
valor_entero1 = 69
valor_decimal1 = 67.69
valor_texto1 = "Gojo"
valor_booleano1 = True
print("Tipos Entrada 1:")
print(type(valor_entero1))
print(type(valor_decimal1))
print(type(valor_texto1))
print(type(valor_booleano1))
#entrada 2
print("- Entrada 2-")
valor_entero2 = 187
valor_decimal2 = 0.99
valor_texto2 = "Jay"
valor_booleano2 = False
print("Tipos Entrada 2:")
print(type(valor_entero2))
print(type(valor_decimal2))
print(type(valor_texto2))
print(type(valor_booleano2))
# --- Ejercicio 8: Convertir tipos ---
print("--- Ejercicio 8 ---")
#entrada 1
print("- Entrada 1-")
texto_num1 = "25"
texto_a_entero1 = int(texto_num1)
print("Texto a int 1:", texto_a_entero1, type(texto_a_entero1))
numero1 = 100
numero_a_texto1 = str(numero1)
print("Int a texto 1:", numero_a_texto1, type(numero_a_texto1))
#entrada 2
print("- Entrada 2-")
texto_num2 = "67"
texto_a_entero2 = int(texto_num2)
print("Texto a int 2:", texto_a_entero2, type(texto_a_entero2))
numero2 = -67
numero_a_texto2 = str(numero2)
print("Int a texto 2:", numero_a_texto2, type(numero_a_texto2))
# --- Ejercicio 9: Booleanos y comparaciones ---
print("--- Ejercicio 9 ---")
#entrada 1
print("- Entrada 1-")
x1 = 8
y1 = 3
mayor1 = x1 > y1
print("¿8 es mayor que 3?:", mayor1)
print(type(mayor1))
#entrada 2
print("- Entrada 2-")
x2 = 10
y2 = 20
mayor2 = x2 > y2
print("¿10 es mayor que 20?:", mayor2)
print(type(mayor2))