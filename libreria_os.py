"""
    Libreira os
    Python, como un lenguaje multiplataforma, es ideal para solventar las incompatibilidades, 
    como la diversidad en la notación de rutas entre sistemas operativos. En este escenario, 
    se recomienda el uso de la librería interna os para resolver facilmente este tipo de problemas.
    
    En Python, os es un módulo que proporciona funciones para interactuar con el sistema operativo. 
    Este módulo es parte de la biblioteca estándar de Python y ofrece métodos para realizar operaciones 
    que involucran el sistema operativo, como manipular archivos, interactuar con el sistema de archivos, 
    obtener información del entorno, ejecutar comandos, entre otros.
"""
# abspath: conocer la ruta absoluta de un directorio o carpeta
import os

print(f"Ruta absoluta: {os.path.abspath('ejemplo_archivo_2.txt')}")

# os.path.join: concatenar rutas para SO
print(f"Ruta con unión: {os.path.join('carpeta','curso_backend_python','pruebajoin.txt')}")
# os.mkdir("E:\polisura\python\\aprendiendo_python\carpeta\curso_backend_python", 750)


#with open("carpeta\curso_backend_python\pruebajoin.txt", "w") as pruebajoin:
#    pruebajoin.write("Esto es una prueba de join\n")

# os.path.basename: obtener el directorio base en donde nos encontramos ubicados
print(os.path.basename(os.path.abspath("ejemplo_archivo_2.txt")))

# os.path.exists: validación de existencia de un directorio o archivo
"""cuando la ruta no existe"""
print(os.path.exists("carpeta\curso_backend_python\pruebajoin.txt"))
"""cuando la ruta existe"""
print(os.path.exists(os.path.abspath("ejemplo_archivo_2.txt")))

