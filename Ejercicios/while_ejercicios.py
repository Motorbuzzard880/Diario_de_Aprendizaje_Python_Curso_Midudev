###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")



contador = 10
while contador > 0:
    print(contador)
    contador -= 1




# # Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")


contador = 0
resultado = 0
while contador <= 20:
    if contador % 2 == 0:
        resultado += contador
    contador += 1
print(f"la suma de los numero pares es: {resultado}")

#Otra solucion mas facil

print("\nEjercicio 2:")

contador = 0
resultado = 0
while contador <= 20:
    resultado += contador
    contador += 2  
    
print(f"La suma de los números pares es: {resultado}")




# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")


numero = int(input("Introduce un número entero positivo: "))
factorial = 1
contador = 1
while contador <= numero:
    factorial *= contador
    contador += 1
print(f"El factorial de {numero} es: {factorial}")



# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")



while True:
    p = input("Introduce una contraseña de al menos 8 caracteres: \n")
    if len(p) >= 8:
        print("contraseña valida")
        break
    else:
        print("La contraseña debe tener al menos 8 caracteres. Inténtalo de nuevo")




# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")

numero = int(input("Introduce un numero: \n"))
print(f"Tabla de multiplicar del numero {numero}: ")
multiplicador = 1
while multiplicador < 11:
    print(f"{numero} * {multiplicador} = {numero * multiplicador}")
    multiplicador += 1


