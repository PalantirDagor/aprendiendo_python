"""
    Metodos de tuplas y sus usos
"""
tupla: tuple = (1,2,3)
print(type(tupla), tupla)
"""Error al ingresar nuevo elemento"""
#tupla[0] = 999
print(tupla[::-1])

"""Escenario en el que usar tuplas"""
tipo_documento: list = ["CC", "TI", "CE", "PASP"]
print("antes : ", type(tipo_documento), tipo_documento)
tipo_documento: tuple = tuple(tipo_documento)
print("despues : ", type(tipo_documento), tipo_documento)

print(len(tipo_documento))
print(tipo_documento[2])
print(tipo_documento[0:3])
