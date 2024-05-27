# 1. Suma de elementos
def suma_elementos(lista):
    return sum(lista)

# 2. Máximo y mínimo
def maximo_minimo(lista):
    return max(lista), min(lista)

# 3. Promedio de una lista
def promedio_lista(lista):
    return sum(lista) / len(lista)

# 4. Elementos mayores que un valor
def elementos_mayores_que_n(lista, n):
    return [elemento for elemento in lista if elemento > n]

# 5. Eliminar duplicados
def eliminar_duplicados(lista):
    return list(set(lista))

# 6. Contar elementos
def contar_elementos(lista, valor):
    return lista.count(valor)

# 7. Invertir lista
def invertir_lista(lista):
    return lista[::-1]

# 8. Concatenar listas
def concatenar_listas(lista1, lista2):
    return lista1 + lista2

# 9. Producto de elementos
def producto_elementos(lista):
    producto = 1
    for elemento in lista:
        producto *= elemento
    return producto

# 10. Encontrar índice
def encontrar_indice(lista, valor):
    if valor in lista:
        return lista.index(valor)
    else:
        return -1

# Ejemplos de uso:
lista_numeros = [1, 2, 3, 4, 5]
valor_n = 3
print("1. Suma de elementos:", suma_elementos(lista_numeros))
print("2. Máximo y mínimo:", maximo_minimo(lista_numeros))
print("3. Promedio de la lista:", promedio_lista(lista_numeros))
print("4. Elementos mayores que", valor_n, ":", elementos_mayores_que_n(lista_numeros, valor_n))
print("5. Lista sin elementos duplicados:", eliminar_duplicados(lista_numeros))
print("6. Veces que aparece", valor_n, "en la lista:", contar_elementos(lista_numeros, valor_n))
print("7. Lista invertida:", invertir_lista(lista_numeros))
lista2 = [6, 7, 8, 9, 10]
print("8. Concatenación de listas:", concatenar_listas(lista_numeros, lista2))
print("9. Producto de elementos de la lista:", producto_elementos(lista_numeros))
print("10. Índice de la primera aparición de", valor_n, ":", encontrar_indice(lista_numeros, valor_n))