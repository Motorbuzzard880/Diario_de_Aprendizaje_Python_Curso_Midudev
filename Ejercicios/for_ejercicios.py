# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")

numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for num in numeros:
    if num % 2 == 0:
        print(num)

"""
Otra Soluciòn

for num in range(2, 21, 2):  #range genera numeros del 2 al 20 (sin incluir 21)
    print(num)               #el ultimo dos es el paso (Step)

"""


# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")


numeros = [10, 20, 30, 40, 50]
suma = 0

for i in numeros:
    suma += i
media = suma / len(numeros)
print(f"La media de la lista es: {media}")






# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")

numeros = [15, 5, 25, 10, 20]
maximo = numeros[0]
for num in numeros:
    if num > maximo:
        maximo = num
print(f"El numero maximo es: {maximo}")




# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")


palabras = ["casa", "arbol", "sol", "elefante", "luna"]
palabra_larga = [palabra for palabra in palabras if len(palabra) > 5]
print(palabra_larga)




# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")


palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
contador = 0
palabras_coincidentes = []                  #Argegado extra (lista para mostrar palabras que coinciden)
letra = input("Introduce una letra: \n")
for palabra in palabras:
    if palabra[0].lower() == letra.lower():
        contador += 1
        palabras_coincidentes.append(palabra)
print(f"En la lista hay {contador} palabras que empiezan con {letra}")
print(palabras_coincidentes)