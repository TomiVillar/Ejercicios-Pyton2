# 1. Contar letras
def contar_letras(cadena):
    frecuencia_letras = {}
    for letra in cadena:
        frecuencia_letras[letra] = frecuencia_letras.get(letra, 0) + 1
    return frecuencia_letras

# 2. Diccionario inverso
def diccionario_inverso(diccionario):
    return {valor: clave for clave, valor in diccionario.items()}

# 3. Merge de diccionarios
def merge_diccionarios(dic1, dic2):
    return {**dic1, **dic2}

# 4. Filtrar diccionario
def filtrar_diccionario(diccionario, lista_claves):
    return {clave: diccionario[clave] for clave in lista_claves if clave in diccionario}

# 5. Diccionario de cuadrados
def diccionario_cuadrados(n):
    return {i: i*i for i in range(1, n+1)}

# 6. Intercambiar valores
def intercambiar_valores(diccionario, clave1, clave2):
    diccionario[clave1], diccionario[clave2] = diccionario[clave2], diccionario[clave1]
    return diccionario

# 7. Sumar valores
def sumar_valores(diccionario):
    return sum(diccionario.values())

# 8. Diccionario de frecuencias
def diccionario_frecuencias(lista_palabras):
    frecuencias = {}
    for palabra in lista_palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias

# 9. Actualizar diccionario
def actualizar_diccionario(diccionario, lista_tuplas):
    diccionario.update(lista_tuplas)
    return diccionario

# 10. Valores únicos
def valores_unicos(diccionario):
    return list(set(diccionario.values()))

# Ejemplos de uso:
cadena = "hola mundo"
print("1. Frecuencia de letras:", contar_letras(cadena))

diccionario = {"a": 1, "b": 2, "c": 3}
print("2. Diccionario inverso:", diccionario_inverso(diccionario))

dic1 = {"a": 1, "b": 2}
dic2 = {"b": 3, "c": 4}
print("3. Merge de diccionarios:", merge_diccionarios(dic1, dic2))

print("4. Filtrar diccionario:", filtrar_diccionario(diccionario, ["a", "b", "d"]))

n = 5
print("5. Diccionario de cuadrados:", diccionario_cuadrados(n))

print("6. Intercambiar valores:", intercambiar_valores(diccionario, "a", "b"))

print("7. Sumar valores:", sumar_valores(diccionario))

lista_palabras = ["hoja", "mundo", "hola", "python"]
print("8. Diccionario de frecuencias:", diccionario_frecuencias(lista_palabras))

lista_tuplas = [("c", 5), ("d", 6)]
print("9. Actualizar diccionario:", actualizar_diccionario(diccionario, lista_tuplas))

print("10. Valores únicos:", valores_unicos(diccionario))