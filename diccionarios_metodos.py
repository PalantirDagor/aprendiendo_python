import pprint

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

"""
    Forma de concatenar utilizando el truco de los ** o *
    KEY ARGS | KARGS: **
    ARGS: *
"""
dic_concat_kargt: dict = {**copia_b, **a_concatenar}
print(dic_concat_kargt)

"""
    Metodo PopItem: Nos devuelve el ultimo item que elimina
"""

llave, valor = dic_concat_kargt.popitem()
print("llave eliminada ", llave, "valor_eliminado de la llave", valor)
print(dic_concat_kargt)

"""
    Metodo Clear: Nos elimina todos los items del diccionario
"""
print("Antes: ", dic_concat_kargt)
dic_concat_kargt.clear()
print("Despues: ",dic_concat_kargt)

"""
    Uso y manejo de los niveles de profundidad dentro de un diccionario

cedula
  datos personales:
    nombres
    apellidos
    estado civil
    fecha nacimiento
    genero
    tipo sangre
      rh
      grupo_sanguineo

  datos de contacto
    telefono
    email
    fax
    celuar
    fijo
    direcciones
      [
        direccion
        estado:
      ]      
  
"""
dict_datos_per: dict = {}
dict_datos_per = {
    "nombre": "pepito",
    "apellidos": "perez",
    "estado_civil": "solteros",
    "fecha_nacimiento": "01/01/2000",
    "genero": "masculino",
    "tipo_sangre": {
      "rh": "+",
      "grupo_sanguineo": "AB"
     }
}

pprint.pprint(dict_datos_per)

datos_contacto = {
    "telefono": "4444444",
    "email": "demo@demo.com",
    "fax": None,
    "celular": "3000000000",
    "fijo": None,
    "direcciones": (
        {
            "direccion": "parque del poblado",
            "estado": "activa"
        },
        {
            "direccion": "el parque del periodista",
            "estado": "inactiva"
        },
    )
}

dict_datos_per["datos de contacto"] = datos_contacto

pprint.pprint(dict_datos_per)

print(dict_datos_per["datos de contacto"]["direcciones"][1]["direccion"])

dict_cedula: dict = {}
dict_cedula["1128456977"] = dict_datos_per
pprint.pprint(dict_cedula)
