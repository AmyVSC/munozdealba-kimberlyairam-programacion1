print("Unidad 2L2 Operadores aritméticos, relacionales y lógicos")
# Ejercicio 1 ¿Es par o impar?
print("--- Ejercicio 1 ---")
numero = 67
es_par = (numero % 2 == 0)
print("El numero", numero, "¿es par?", es_par)
# Ejercicio 2 Concatenar vs. sumar
print("--- Ejercicio 2 ---")
texto_1 = "6"
texto_2 = "7"
print("Concatenacion:", texto_1 + texto_2)
print("Suma numerica:", int(texto_1) + int(texto_2))
# Ejercicio 3 Mini reporte de un perfil
print("--- Ejercicio 3 ---")
nombre = "Airam"
edad = 18
estatura = 1.52
es_estudiante = True
print("Reporte de perfil:")
print("Nombre:", nombre, "-> Tipo:", type(nombre))
print("Edad:", edad, "-> Tipo:", type(edad))
print("Estatura:", estatura, "-> Tipo:", type(estatura))
print("¿Es estudiante?:", es_estudiante, "-> Tipo:", type(es_estudiante))
mensaje_extra = nombre + " tiene " + str(edad) + " años."
print("Extra:", mensaje_extra)
# Ejercicio 4 Operadores aritméticos básicos
print("--- Ejercicio 4 ---")
num_a = 1877
num_b = 707
print("Aritmética:")
print("Suma:", num_a + num_b)
print("Resta:", num_a - num_b)
print("Multiplicación:", num_a * num_b)
print("División:", num_a / num_b)
# Ejercicio 5 División entera y módulo
print("--- Ejercicio 5 ---")
print("División entera (//):", num_a // num_b)
print("Módulo o residuo (%):", num_a % num_b)
# Ejercicio 6 Operadores relacionales
print("--- Ejercicio 6 ---")
mayor_que = (num_a > num_b)
menor_que = (num_a < num_b)
es_igual = (num_a == num_b)
es_diferente = (num_a != num_b)
print("¿Es mayor?:", mayor_que)
print("¿Es menor?:", menor_que)
print("¿Es igual?:", es_igual)
print("¿Es diferente?:", es_diferente)
# Ejercicio 7 Operadores lógicos
print("--- Ejercicio 7 ---")
y = (num_a > num_b) and (num_a < 2000)
o = (num_a > num_b) or (num_a < 1000)
condicion_not = not (num_a == num_b)
print("Resultado AND:", y)
print("Resultado OR:", o)
print("Resultado NOT:", condicion_not)
# Ejercicio 8 Promedio y aprobación
print("--- Ejercicio 8 ---")
calif_1 = 7.6
calif_2 = 6.7
calif_3 = 9.6
promedio = (calif_1 + calif_2 + calif_3) / 3
aprobado = (promedio >= 6)
print("Promedio obtenido:", promedio)
print("¿Está aprobado?:", aprobado)
# Ejercicio 9 Validación de elegibilidad
print("--- Ejercicio 9 ---")
edad_persona = 19
nacionalidad = "mexicana"
es_elegible = (edad_persona > 17) and (nacionalidad == "mexicana")
print("¿Es elegible?:", es_elegible)
es_elegible_or = (edad_persona > 17) or (nacionalidad == "mexicana")
print("Extra:", es_elegible_or)