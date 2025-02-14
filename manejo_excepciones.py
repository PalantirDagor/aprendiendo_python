"""
    Manejo de Excepciones en Python
    Incluso si una declaración o expresión es sintácticamente correcta, 
    puede generar un error cuando se intenta ejecutar. Los errores detectados 
    durante la ejecución se llaman excepciones, y no son incondicionalmente fatales
"""
# modo simple

# 1/0

try:
    print("999")
    1/0
except:
    print("no se puede dividir por cero")
    print("otras acciones")

print("Todo esta bien, me protegio el 'try - except'")

# modo simple
# Exception es el papá de las excepciones (similar a object)
print("*" * 50)
try:
    print("999")
    1/0
except ZeroDivisionError as ex:
    print(f"excepción específica:'{ex}'")
    print("otras acciones")
except Exception as ex:
    print(f"el error que se presentó es:'{ex}'")
    print("otras acciones")

print("*" * 50)
try:
    print(nombre)
except ZeroDivisionError as ex:
    print(f"excepción específica:'{ex}'")
    print("otras acciones")
except NameError:
    print("la variable no está definida")
except Exception as ex:
    print(f"el error que se presentó es:'{ex}'")
    print("otras acciones")

# un truco es que uno muchas veces puede forzar la excepción
# para que no siga ejecutando lo demás
# detectan que el hash cambió: corrupto o fue hackeado, etc.

# raise [Exception(....)]
print("*" * 50)
try:
    print("uno")
    raise 
    print("dos")
except:
    print("pasó un error x")

print("*" * 50)
try:
    print("uno")
    raise Exception("estoy caprichoso, quise lanzar un error")
    print("dos")
except Exception as ex:
    print(f"error generado -->: {ex}")

# Finally
# todo ok
print("*" * 50)
try: # obligatorio
    print("1. TODO BIEN")
except: # obligatorio
    print("-1. Bloque de captura de excepción. Nota: permite múltiple except")
else: # opcionales
    print("2. Bloque después de terminado el bloque 1")
finally: # opcionales
    print("3. Bloque que siempre se ejecuta")

# ejemplo con error provocado con raise
print("*" * 50)
try: # obligatorio
    print("1. TODO MAL")
    raise
except: # obligatorio
    print("-1. Bloque de captura de excepción. Nota: permite múltiple except")
else: # opcionales
    print("2. Bloque después de terminado el bloque 1")
finally: # opcionales
    print("3. bloque que siempre se ejecuta")
