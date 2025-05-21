# Ejercicio_01:
# Escribe una función llamada invertir_palabra que reciba una cadena de texto (string)
# y devuelva esa misma palabra pero invertida.

def invertir_palabra(palabra):
    invertir = palabra[::-1]
    return invertir

print(invertir_palabra("Python"))



# Ejercicio_02
# Escribe una función llamada contar_vocales que reciba una cadena de texto (string) y devuelva cuántas vocales (a, e, i, o, u) 
# tiene, sin diferenciar mayúsculas y minúsculas.




def contar_vocales(string):
    contador = 0
    string = string.upper()  # Convertimos a mayúsculas para simplificar
    for letra in string:
        if letra in "AEIOU":  # Verificamos si la letra es una vocal
            contador += 1
    return contador

print(contar_vocales("Corazon"))



#ejercicio_03:
# Escribe una función llamada es_palindromo que reciba una cadena y devuelva True si la palabra es un palíndromo
# (se lee igual al derecho y al revés), o False si no lo es.

palabra = input("Introduce una palabra: ")
def es_palindromo(palabra):
    palabra = palabra.upper()
    return palabra == palabra[::-1]

if es_palindromo(palabra):
    print(f"{palabra} es un palíndromo. ¡Correcto!")
else:
    print(f"{palabra}, no es un palindromo")



# Ejercicio_04 Calcular el área de un triángulo
# Escribe una función llamada area_triangulo que reciba la base
# y altura de un triángulo y devuelva su área.

def area_triangulo(base, altura):
    """
    Calcula el área de un triángulo dado su base y altura.
    Args:
        base (int/float): Base del triángulo. Debe ser un valor positivo.
        altura (int/float): Altura del triángulo. Debe ser un valor positivo.
    Returns:
        float: Área del triángulo (base * altura / 2). 
        Retorna 0.0 si la base o altura son <= 0 (inválidos)."""

    if base <= 0 or altura <=0:
        return 0.0
    return float(base * altura / 2.0)

print(f"El aera del triangulo es: {area_triangulo(5,-4)}")