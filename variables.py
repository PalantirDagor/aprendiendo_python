"""
    Archivo para el manejo de las variables en python 
    comentario comillas dobles
    ''
"""
'''
    Este comentario esta generado con comillas simples
    "hola este comentario tiene dos comillas dobles"
'''

# un comentario con numeral!!

"""
    [] = corchetes
    {} = llaves
    () = paréntesis
"""

"""Tipos de datos y variables Python"""
"""Datos Enteros (int)"""
numero_entero: int = 1

"""Datos Flotantes (float)"""
numero_decimal: float = 5.2

"""Datos de Texto (str)"""
variable_texto: str = 'Este es mi primer texto en el "backend python"'
print(variable_texto[:7])

"""Variables Booleanas (bool)"""
verdadero: bool = True
falso: bool = False

"""Variables Listas (list)"""
"""
    Recordar que la posicion o el indice en las 
    estructuras de datos de las listas, tuplas o diccionarios
    comienzan desde 0
"""
lista_numeros: list = [1, 2, 3, 4, 5]
lista_textos: list = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
lista_booleanos: list = [True, False, True, False, True]
lista_mixma: list = [True, 1, 'hola']

"""Variables Tuplas (tuple)"""
tupla_1: tuple = (1, 2, 3, 4, 5, 6)
lista_tuplas: list = list(tupla_1[1:4])
print(lista_tuplas)

"""Variables Conjuntos (set)"""
mi_set: set = {1, 'pero', 2, 2, 2, 2, 'pero', 'pero'}
print(mi_set)

"""Variables Diccionarios (dict)"""
mi_diccio_nombres: dict = {'nombre_1': 'Andres', 'nombre_2': 'Joaquin', 'nombre_3': 'Santiago'}
print(mi_diccio_nombres['nombre_2'])

"""Variables None (NoneType)"""
None 
