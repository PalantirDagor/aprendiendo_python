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
