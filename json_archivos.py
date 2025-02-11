""" 
    JSON
    JSON (JavaScript Object Notation), que significa Notación de Objetos de JavaScript, 
    es un formato de intercambio de datos ligero y legible por humanos. Se utiliza 
    para representar y transmitir datos estructurados entre un servidor y un cliente, 
    o entre diferentes componentes de una aplicación. A continuación, se resumen algunos 
    aspectos clave de JSON:
    
    string: cadenas de texto
    number: numeros sean cualquiera
    object: obejtos reprentados con {}
    array: listas representadas con []
    true/false: datos booleanos
    null: dato nulos, sin valor
    
    EJEMPLO

    {
        "cadena": "Esto es una cadena de texto",
        "numero": 42,
        "decimal": 3.14159,
        "verdadero": true,
        "falso": false,
        "nulo": null,
        "lista": [1, 2, 3, 4, 5],
        "objeto": {
            "clave1": "valor1",
            "clave2": "valor2"
        }
    }
    
    MAPEO JSON VS PYTHON
    
    Python type                             JSON value
    dict  -->   Libreia json.jsonencoder --> object
    list  -->   Libreia json.jsonencoder --> array
    str  -->    Libreia json.jsonencoder --> string
    True  -->   Libreia json.jsonencoder --> true
    False  -->  Libreia json.jsonencoder --> false
    None  -->   Libreia json.jsonencoder --> null
    
    Funciones de la libreria JSON
    
    dump  -> guardo un dict dentro de un archivo
    dumps -> convierto un dict a json a nivel de memoria (asignada a un string)
    load  -> carga archivos json a diccionario
    loads -> carga json en texto a diccionario
"""
import json

datos: dict = {
    "nombre":"demo",
    "apellido":"Agudelo",
    "fecha_nacimiento":"16/11/87",
    "grupo_sanguineo":{
        "rh":"+",
        "grupo":"O"
    },
    "activo": True,
    "antecedentes": None,
    "tags": ["aa", "bb", "cc"]
}

datos_profe: dict = {
    "nombre":"Duber",
    "apellido":"Galvis",
    "rol": "Profe en Polisura",
    "fecha_nacimiento":"19/11/87",
    "grupo_sanguineo":{
        "rh":"+",
        "grupo":"O"
    },
    "activo": True,
    "antecedentes": None,
    "tags": ["aa", "bb", "cc"]
}

# dumps
variable = json.dumps(datos)
print(json.dumps(datos))

print(json.dumps(datos, indent=4))

print(type(variable))
# print(variable["grupo_sanguineo"]["rh"]) # error, no es un dict

texto_json_a_dict = json.loads(variable)
print(texto_json_a_dict)
print(type(texto_json_a_dict))
print(texto_json_a_dict["grupo_sanguineo"])

# dump
with open("datos_persona_2.json", "w") as fl:
    json.dump(datos_profe, fl, indent=4)

# load
with open('datos_person.json') as fl:
    jso_to_dic = json.load(fl)
    print(jso_to_dic)
    print(type(jso_to_dic))    

