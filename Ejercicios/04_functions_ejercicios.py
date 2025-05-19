# Ejercicio 1: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().

def definir_multiplo(multiplo):
    for num in range(multiplo, 51, multiplo):
        print(num)

definir_multiplo(25)



# Ejercicio 2: Tabla de multiplicar
# una funcion que devuelva la tabla de multiplicar de un numero




def tabla_multiplicar(numero):
    for multiplicador in range(1, 11):
        print(f"{numero} * {multiplicador} = {numero * multiplicador}")

tabla_multiplicar(5)



# Ejercicio 3: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().

def suma_rango(inicio, fin):
    """Suma todos los números en el rango [inicio, fin] (inclusive)."""
    return sum(range(inicio, fin + 1))

print(suma_rango(1, 200))