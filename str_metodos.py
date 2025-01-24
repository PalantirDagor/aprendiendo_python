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
print(variable_cadena.startswith("@"))
"""Metodo Capitalize: nos permite tener en una cadena de texto su
    primera letra en mayuscula"""
print(variable_cadena.lower().capitalize())
"""Metodo Title: me permite colocar en mayuscula todas las palabras de una cadena 
    de texto"""
print(variable_cadena.title())
"""Metodo Center: nos permite centrar"""
curso: str = variable_cadena
print(curso)
print(curso.center(60, " "))
print(curso.center(60, "-"))
print(curso.center(60, "_"))
print(curso[6:].upper().center(60, "@"))
"""Metodo Len: nos permite conocer la longitud de la cadena de texto"""
print("El texto es --> ", curso, " Y su tamaño es: ", len(curso))
print("El texto es --> ", " ", " Y su tamaño es: ",len(" "))
"""Metodo Rjust: nos permite darle caracteres o espacios a una cadena de texto
en la parte derecha de esta o al principo"""
print(curso.rjust(1, "*"))
variable: str = curso.rjust(10, "*")
# imprime lo siguiente
#**********Curso de backend con python
print(variable)
"""Metodo Ljust: nos permite darle caracteres o espacios a una cadena de texto
en la parte izquierda de esta o al principo"""
print(curso.ljust(10, "*"))
# imprime lo siguiente
#Curso de backend con python**********
"""Metodo ZFILL, nos permite añadir ceros a la cadena de texto en la parte derecha
de la misma con el numero deseado"""
print(curso.zfill(10))
# imprime lo siguiente
# 0000000000Curso de backend con python
"""Metodo Replace: nos permite reemplazar partes de la cadena de texto
con otro texto deseado"""
print("Cadena de texto original: ", curso)
print("Cadena de texto reemplazada: ", curso.replace(" ", "."))
print("Cadena de texto reemplazada: ", curso.replace("python", "Java"))
print("Cadena de texto que no encuentra: ", curso.replace("Go", "C#"))
"""Metodo Count: nos permite validar el numero de veces que se repite una palabra
cadena de texto o caracter"""
print("Cuantas 'a' hay en el texto?: ", curso.count("a"))
print("Cuantas 'A' hay en el texto?: ", curso.count("A"))
print("Cuantas 'con' hay en el texto?: ", curso.count("con"))
print("Cuantas 'o' hay en el texto?: ", curso.count("o"))
"""Metodo Find: nos permite buscar en la cadena de texto si existe la palabra, caracter
o simbolo a buscar"""
print("La posición donde esta la 'o'?: ", curso.find("o"))
print("La posición donde esta la 'y'?: ", curso.find("y"))
print("La posición donde esta la 'Y'?: ", curso.find("Y"))
print("La posición donde esta 'python'?: ", curso.find("python"))
print("La posición donde esta la 'javascript'?: ", curso.find("javascript"))
"""Metodo Rstrip: nos permite eliminar espacios en blanco en la parte derecha 
de la cadena de texto"""
curso_con_r_espacios: str = "        " + curso
print("Se imprime con espacios: ", curso_con_r_espacios)
print("Uso de Rstrip --> ", curso_con_r_espacios.rstrip())
"""Metodo Rstrip: nos permite eliminar espacios en blanco en la parte izquierda 
de la cadena de texto"""
curso_con_l_espacios: str = curso + "        "
print("Se imprime con espacios: ", curso_con_l_espacios, len(curso_con_l_espacios))
print("Uso de lstrip --> ", curso_con_l_espacios.lstrip())
"""Metodo Strip: es metodo nos permite eliminar espacios tanto en derecha como en 
izquierda de la cadena de texto"""
print("Original: ", curso_con_r_espacios, len(curso_con_r_espacios),  
    ". Sin espacios: ", curso_con_r_espacios.strip(), len(curso_con_r_espacios.strip()))
# espacios a la izquierda
print("Original: ", curso_con_l_espacios, len(curso_con_l_espacios),
    ". Sin espacios: ", curso_con_l_espacios.strip(), len(curso_con_l_espacios.strip()))
#espacios en ambos lados
espacios_curso: str = "        " + curso + "       "
print("Original: ", espacios_curso, len(espacios_curso),
    " Sin espacios: ", curso_con_l_espacios.strip(), len(curso_con_l_espacios.strip()))
"""Metodo Index: """
print("Utilizando Index: ", curso.index("y"))
#print("Utilizando Index con error: ", curso.index("Z"))
print("Utilizando Index: ", curso.index("python"))
"""Metodo SPLIT: nos permite separar o rebanar nuestra cadena de texto segun un
caracter indicado"""
print("Usando el metodo Split: ", curso.split(" "), len(curso.split(" ")))
print(curso.split(" ")[3])
print(curso.split("o"))
"""Metodos is..."""
print(curso.islower())
print(curso.isdigit())
print(curso.lower().islower())
print(curso.isupper())
print(curso.upper().isupper())
"""Multipicación de texto"""
print("@" * 5)
print(curso * 3)
print([1, 2 , "--", "A"] * 4)
"""Saltos de linea en cadenas de texto"""
curso_salto_linea: str = "Curso\nde\nbackend\ncon\npython"
print(curso_salto_linea)










