"""
    Metodos generales en Python
"""

"""
    HARCODEADO (HARDCODING)
    malas prácticas
"""
"""Mala practica"""
print("Esto es una mala practica HARDCODING")
print("Esto es una mala practica HARDCODING")
print("Esto es una mala practica HARDCODING")
print("Esto es una mala practica HARDCODING")
print("Esto es una mala practica HARDCODING")
print("Esto es una mala practica HARDCODING")

mensaje: str = "Esto es una buena practica que evita el HARDCODING"
mensaje2: str = "Esto es una mala practica HARDCODING"

num_mensaje1: int = 1
#num_mensaje: int = input("ingrese el nummero del mensaje: ")

#print(mensaje, " ", num_mensaje)
print(mensaje, " ", num_mensaje1)
#print(mensaje," ", num_mensaje)
print(mensaje, " ", num_mensaje1)

"""
    Metodos de Casteo o constructores
"""

str_num_1: str = "1"
print(str_num_1)
print(type(str_num_1))

"""
    Casteo de cadena de texto a numero
"""
int_num_1: int = int(str_num_1)
print(int_num_1)
print(type(int_num_1))

"""
    Casteo de numero a cadena de texto
"""
nuevo_srt_num_1: str = str(int_num_1)
print(nuevo_srt_num_1)
print(type(nuevo_srt_num_1))

"""
    Casteo de cadena de texto a decimal
"""
float_num_1: float = float(str_num_1)
print(float_num_1)
print(type(float_num_1))

"""
    No es permitido, solo valores equivalentes en el mundo de los enteros
"""
num_str: str = "1a"
#num_int: int = int(num_str)
#print(num_int)
#print(type(num_int))

"""
    Metodos de casteo para estructuras de datos
"""
print(type(tuple([1,2,3])), ": ", tuple([1,2,3]))
print(type(list({1,2,3})), ": ", list({1,2,3}))
print(type(set((4,5,6,6))), ": ", set((4,5,6,6)))

""""
    Metodo TYPE() nos permite validar el tipo de objeto o variable
"""
print(type(1), ": ", 1)
print(type(1.0), ": ", 1.0)
print(type(True), ": ", 1.0)
print(type([1,2]), ": ", [1,2])
print(type((1,2)), ": ", (1,2))
print(type({1,2}), ": ", {1,2})
print(type({"nombre": "Santiago"}), ": ", {"nombre": "Santiago"})
print(type(None), ": ", "None")

"""
    Metodo ISINSTANCE, Evalua el tipo de objeto o variable
"""
print("Evaluacion simple")
print(isinstance(num_str, str))
print(isinstance(float_num_1, int))


print("Evaluacion multiple")
print(isinstance(num_str, (str, int)))
print(isinstance(float_num_1, (int, list)))

"""Metodo Print y sus caracteristicas"""
"""Print simple Hardcodeado"""
print("Hola mundo")
"""Print simple con variable"""
print(float_num_1)
"""Print Multiple"""
print(str_num_1, nuevo_srt_num_1, float_num_1, "Hola numeros")
"""Print sep nos permite inprimir entre las variables el valor que deseemos"""
print(str_num_1, nuevo_srt_num_1, float_num_1, sep = " -- ")
"""Print End, nos permite imprimir algo al finalizar las variables impresas"""
print(str_num_1, nuevo_srt_num_1, float_num_1, end = "&&")

"""
    Metodo HELP: este metodo me permite conocer la documemntación de los
    diferentes metodos en Python
"""
help(str.center)
help(int.bit_length)
