# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos  ✅
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.


lista1 = [1, 2, 3, 4, 5]
lista1.append(6)
lista1.insert(2, 10)
lista1[0] = 0
print(lista1)





# Ejercicio 2: Combinar y limpiar listas  ✅
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().


lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
lista_a.extend(lista_b)
lista_a.remove(1)
pop = lista_a.pop(3)
lista_b.clear()
print(pop)
print(lista_b)







# Ejercicio 3: Slicing y eliminación con del  ✅
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.


lista3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del lista3[2:5]
print(lista3)



# Ejercicio 4: Ordenar y contar ✅
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.


lista1 = [5, 2, 8, 1, 9, 4, 2]
lista1.sort()
contador = lista1.count(2)
print(f"El numero 2 aparece {contador} veces")
comprobar = (7 in lista1)
print(f"El numero 7 esta en la lista?: {comprobar}")
print(lista1)





# Ejercicio 5: Copia vs. Referencia   ✅
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.


original = [1, 2, 3]
copia1 = original[:]
copia2 = original.copy()
referencia = original
referencia[0] = 10
print("original:", original)       
print("copia1:", copia1)           
print("copia2:", copia2)        
print("referencia:", referencia)   




# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.   ✅
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.


frutas = ["Manzana", "pera", "BANANA", "naranja"]
frutas.sort(key=str.lower)
print(frutas)