"""
    Funciones
    
    La función es un bloque de código reutilizable que realiza una tarea 
    específica cuando se llama o se invoca. Las funciones se utilizan 
    para organizar y modularizar el código, lo que facilita la comprensión 
    y el mantenimiento de programas más grandes. Cada función en Python 
    tiene un nombre y puede recibir argumentos (valores de entrada) y devolver 
    un resultado (valores de salida).

    USAR FUNCIONES ES LA CLAVE PARA:

    Programación funcional
    Programación orientada a objetos
    Programación orientada a procedimientos
"""

# función sin parametros y sin retorno
# definición
def imprimir_saludo():
  print("*" * 10)
  print("Hola a tod@s!")
  print("*" * 10)


# llamado de una función
imprimir_saludo()

# función con parametros y sin retorno
def imprimir_saludo_2(nombre:str):
  longitud_ast = len(nombre) + 12
  print("*" * longitud_ast)
  print("Hola a: " + nombre)
  print("*" * longitud_ast)

imprimir_saludo_2("Santiago")

"""
    función sin parametros y con retorno
    
    Los retornos los utilizamos siempre y cuando queremos utilizar afuera 
    de la función el valor calculado. Las variables definidas dentro de una 
    función, solamente existen dentro de la misma, y a esto lo llamaremos ámbito.
    
    return retornar algo (simple o múltiple)
"""
def encabezado_simple():
    saludo: str = """

    ___      _   _
    | _ \_  _| |_| |_  ___ _ _
    |  _/ || |  _| ' \/ _ \ ' \\
    |_|  \_, |\__|_||_\___/_||_|
        |__/
      Polisura
    """
    
    return saludo

valor_retornado = encabezado_simple()
print(valor_retornado)

# funcion con parametros y con retorno
def encabezado_simple_2(nombre_empresa: str):
    saludo = f"""

    ___      _   _
    | _ \_  _| |_| |_  ___ _ _
    |  _/ || |  _| ' \/ _ \ ' \\
    |_|  \_, |\__|_||_\___/_||_|
        |__/
        {nombre_empresa}
    """

    return saludo

valor_retornado = encabezado_simple_2("Desarrollador Andres")
print(valor_retornado)

# función con parametros y con multiples retornos
def encabezado_simple_3(nombre_empresa: str):
    saludo = f"""

    ___      _   _
    | _ \_  _| |_| |_  ___ _ _
    |  _/ || |  _| ' \/ _ \ ' \\
    |_|  \_, |\__|_||_\___/_||_|
        |__/
        {nombre_empresa}
    """
    print(saludo)
    longitud = len(saludo)
    nombre_mayuscula = nombre_empresa.upper()
    valor_pi = 3.1416

    return valor_pi, longitud, nombre_mayuscula

valor_retornado = encabezado_simple_3("Backend")
print(valor_retornado, type(valor_retornado))
val_1, val_2, val_3 = valor_retornado
print(val_1, val_2, val_3)

"""
    Args = args
    * --> tupla

    Definir argumentos dinámicos
"""
print("*" * 30)
def suma(*mimamamemima):
  print(type(mimamamemima))
  print(mimamamemima)
  print(mimamamemima[::-1])

suma(1,2,3,4,5,6,7,8,9)

"""
    KARGS
    ** --> diccionario

    Definir argumentos dinámicos
"""
print("-" * 50)
def set_config(**data): # definir config
  print(type(data))
  print(data)
  print(data.keys())

set_config(nombre="Pepito", version=1.0, cloud_provider="aws", sparkmaster ="ss")

"""
    Argumentos opccionales
"""
print("-" * 50)
def opciones(nombre_app: str = "por defecto", version_app:float = 1.0):
  print(f"nombre_app : {nombre_app}")
  print(f"version_app : {version_app}")


# Ejecuación sin argumentos
opciones()

# Ejecución con argumentos
# con argumentos posicionales o posicionalmente
opciones("yoda")
# con los dos parametros
opciones("yoda", 1.5)

# Llamado por argumento
opciones(version_app=0.32)
opciones(version_app=0.39, nombre_app="Duvan_app")

"""Funciones como objeto"""
def suma_dinamica(*valores: list):
  print(f"longitud --> {len(valores)}")
  print(f"total    --> {sum(valores)}")

# Asignar la función a una variable
datos = suma_dinamica

print("Forma original : --")
suma_dinamica(1,2,3,4)
print("*" *20)
print("Forma alias : --")
datos(1,2,3,4,5)

# metodos magicos, ya estan definidos | 
# el nombre de la funcion real se obtiene con __name__
print("nombre de la funcion en la variable: ", datos.__name__)

"""
    Funciones Anidadas
"""
# Funciones de tipo normal
print("*" *20)
def obtener_tipo_salud(genero: str) -> str:
  funcion_devolver  = None
  def mujer(nombre):
    return f"es una mujer, y su nombre es: {nombre}"

  def hombre(nombre):
    return f"es un hombre, y su nombre es: {nombre}"

  if genero == "F":
    funcion_devolver = mujer
    print(mujer("prueba dummy - llamado interno"))
  else:
    funcion_devolver = hombre

  return funcion_devolver

#1. Está retornando netamente la función a utilizar
resultado = obtener_tipo_salud("F")
print(type(resultado))
print(resultado)
print(resultado.__name__)

#2. Yo estoy llamando la función que me devolvió el punto 1 y la estoy ejecutando
print("*" *20)
resultado2 = resultado("PEPITO")
print(type(resultado2))
print(resultado2)

# Funciones del tipo embebidas!! solo funciona de la versión 3.10 asia abajo.
print("*" *20)
def obtener_tipo() -> str:
    def mujeres(nombre):
        return f"es una mujer, y su nombre es: {nombre}"
    return mujeres

print("llego")
obtener_tipo()("Maria Alejandra")
nombre = obtener_tipo()
print(type(nombre))
nombre("Maria Alejandra")
print(nombre.__name__)
print("termino")

"""
    Closure
    Significa que una función de cierre recuerda y puede 
    utilizar variables de su entorno padre
"""
print("*" *20)
def semilla(valor_semilla):
  def ejecutador(numero):
    return numero + valor_semilla
  return ejecutador

set_seed = semilla(0.001)
print(type(set_seed))
print(set_seed)
print(set_seed.__name__)

print(set_seed(5))
print(set_seed(1))
print(set_seed(2.5))
