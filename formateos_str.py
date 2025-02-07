"""
    Format
    El formateo de caracteres en un lenguaje de programación se refiere al 
    proceso de dar formato o estructura a una cadena de caracteres o 
    texto según ciertas especificaciones o patrones. El objetivo principal 
    del formateo de caracteres es presentar datos de una manera legible y 
    estética, lo que es especialmente importante cuando se trata de 
    datos de salida que serán visualizados por humanos.
"""
"""
    Formato Sencillo (Mas utilizado y comun en python ver.3)
    IMPORTANTE = igual número de llaves, igual número de variables
"""
help(str.format)
# Simple

pi: float = 3.1415926535897932384626
nombre: str = "demo.python.format"
print("*" * 50)
mensaje = "el nombre es: {}, el valor de pi es: {}"
print(mensaje.format(nombre, pi))
# Por index (indice)
print("*" * 50)
print("el nombre es: {1}, el valor de pi es: {0}".format(pi, nombre))

# De manera matricial o matricialmente
print("*" * 50)
lista_1 = [111,"pepito", []]
lista_2 = [True, False, pi]
# formatea cualquier tipo
print("el nombre es: {}, el valor de pi es: {}".format(lista_1, lista_2))
# accediendo
print("el nombre es: {0[1]}, el valor de pi es: {1[2]}".format(lista_1, lista_2))

# Kwargs o kargs
print("nombre {name}, edad: {age}".format(age=21, name="luis"))

# Formato con diccionarios
template: str = """
    {ciudad}, Estado, Código Postal
    fecha: {fecha}

    Estimado/a {persona}:

    Mi don {persona}, deseamos informarle que {motivo}.
    Atentamente,

    enviado desde la ciudad de {ciudad}, en la fecha {fecha}
    att: {persona}
"""

datos = {
  "ciudad": "Medellín",
  "fecha": "06/02/2025",
  "persona": "Pepit@",
  "motivo": "DEMO PYTHON MODULO BACKEND"
}

print(template.format(**datos))

elementos = [
    {
        "ciudad": "Medellín",
        "fecha": "06/02/2025",
        "persona": "pepit@",
        "motivo": "DEMO PYTHON MODULO BACKEND"
    },
    {
        "ciudad": "Medellín",
        "fecha": "06/02/2025",
        "persona": "Duber",
        "motivo": "El profe infractor le llegan 8 alumnos mas al modulo tres de Frontend"
    }
]

for dato in elementos:
  print(type(dato))
  print("*" * 30)
  print(template.format(**dato))

"""
    Funciones Avanzadas en el formateo de datos
    <         = delimitación hacia la izquierda
    >         = delimitación hacia la derecha
    ^         = delimitación centrada
    +         = asignación de signo
    :.#[type] = la cantidad de posiciones que se muestra en el elemento

    {[ posicion  vector formato ]}
    posicion = posición del argumento

    **Nos** permite separar el índice o alias del formato con que queramos 
    presentar las variables.
"""
# Asignación de signo
print("*" * 30)
for valor in range(3,-3,-1):
    print("{0:+}".format(valor))

# Segmentacion o la cantidad de posiciones que se muestra en el elemento
print("*" * 30)
print(nombre)
print("{:.4}".format(nombre))

# Estandarización de longitudes
print("*" * 30)
numeros: list = [10, 100, 1000, 10000]
for numero in numeros:
  print("{:10} es múltiplo de 10".format(numero))

# Alineación izquierda
print("*" * 30)
for numero in numeros:
  print("{:<{cantidad}} es múltiplo de 10".format(numero, cantidad=10))
  
# centrado
print("*" * 30)
for numero in numeros:
  print("{:^{cantidad}} es múltiplo de 10".format(numero, cantidad=10))

# derecha
for numero in numeros:
  print("{:>{cantidad}} es múltiplo de 10".format(numero, cantidad=10))
  
# Relleno hacia la derecha
for numero in numeros:
  print("{:0>{cantidad}} es múltiplo de 10".format(numero, cantidad=10))
print("*" * 30)
for numero in numeros:
  print("{:!>{cantidad}} es múltiplo de 10".format(numero, cantidad=10))
