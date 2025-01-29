"""
    Diccionarios en Python y sus metodos y usos
"""
dvacio: dict = {}
dinicializado = {"llave": "valor", "edad": 18.5}
print(type(dinicializado), dinicializado)
"""Forma permitida para acceder a un diccionario"""
print(dinicializado["edad"])
"""Forma no permitida para acceder a un diccionario"""
#print(dinicializado.edad)
"""Accediando a una llave que no existe"""
#print(dinicializado["dígame_el_futuro"])
"""Metodo Get:acceder de manera segura a un diccionario sin generar una excepción"""
print(dinicializado)
print(dinicializado.get("dígame_el_futuro","muestra que no se encuentra la llave"))
"""Cuando si existe la llave"""
print(dinicializado.get("edad", True))
print(dinicializado)
"""Metodo Keys: nos permite conocer las llaves del diccionario (solo las 
llaves de primer nivel)"""
print(dinicializado.keys())
print(list(dinicializado.keys()))
lista_de_llaves: list = list(dinicializado.keys())
print(dinicializado[lista_de_llaves[1]])
"""Metodo Values: nos permite obtener los valores de cada una de las llaves"""
print(dinicializado.values())
print(list(dinicializado.values()))
"""Metodo Items: nos permite separar cada llave-valor en una lista con estos
elementos"""
print(dinicializado.items())
items = list(dinicializado.items())
print(items)

print(items[0])
print(items[0][0])

elemento_1, elemento_2 = list(dinicializado.items())
print("elemento_1:",elemento_1)
print("elemento_2:",elemento_2)

"""Asignación: asignamos valores a las llaves en el diccionario"""
dinicializado["python_nivel"] = 1
print(dinicializado)

dinicializado["python_nivel"] = 2
print(dinicializado)

"""Metodo Pop: Elimina el item de la llave especificada"""
print(dinicializado)
dinicializado.pop('llave')
print(dinicializado)
"""Metodo Copy: nos entrega una copia exacta del diccionario al que se le aplico
el metodo"""
copia_a: dict = dinicializado.copy()
copia_b: dict = dinicializado.copy()
print("copia a: ", copia_a)
print("copia b:", copia_b)

"""Metodo Update: nos permite concatenar dos diccionarios"""
a_concatenar: dict = {"nombre": "Joaquin", "Edad": 20, "Estudia?": True}
print(a_concatenar["nombre"])
print("antes",copia_a )
copia_a.update(a_concatenar)
print("después",copia_a )

