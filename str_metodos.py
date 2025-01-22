"""
    En este archivo veremos los metodos mas comunes para las cadenas de texto
    para su tratamiento, modificacion y manipulación.
"""
variable_cadena: str = "Curso de backend con python"

"""
    SLICES: Manipular elementos de una lista de diferentes formas:
"""
java: str = "Java"
print(variable_cadena[0:20], java)
"""Utilizando el metodo input para ingresar por consola el dato que deseemos"""
#print(variable_cadena[0:20] + " " + input("ingrese el lenguaje de programación deseado"))
"""Diferentes tipos de SLICES"""
print(variable_cadena[:16])
print(variable_cadena[5:])
print(variable_cadena[:-1])
print(variable_cadena[:-2])
print(variable_cadena[-20:])
print(variable_cadena[:])

"""SLICES sin los puntos ':'"""
"""indices positivos"""
print("Positivo: ", variable_cadena[5])
"""Indices negativos"""
print("Negativo: ", variable_cadena[-6])

"""
    Rangos: nos permite crear cadenas de texto con rangos definidos
"""
print(variable_cadena[::])
print(variable_cadena[::2])
print(variable_cadena[::3])
print(variable_cadena[::-1])

"""PRINCIPALES OPERACIONES DE LOS STRINGS"""
"""Metodo Lower: me permite colocar en minusculas una cadena de texto"""
print(variable_cadena.lower())
"""Metodo Upper me permite colocar la cadena de texto en mayusculas"""
print(variable_cadena.upper())
"""Metodo Startwith: me permite evaluar una cadena de texto con un valor dado en
    en el metodo"""
print(variable_cadena.startswith("C"))
print(variable_cadena.startswith("c"))
"""Metodo Capitalize: nos permite tener en una cadena de texto su
    primera letra en mayuscula"""
print(variable_cadena.lower().capitalize())
"""Metodo Title: me permite colocar en mayuscula todas las palabras de una cadena 
    de texto"""
print(variable_cadena.title())








