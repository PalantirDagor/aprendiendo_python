"""
    Manejo de Archivos en Python
    Entender un concepto elemental en el tema de rutas:
        Ruta absoluta: parte de la unidad hasta la ubicación del archivo o carpeta
        Ruta relativa: a partir del lugar donde se encuentre ubicado, usted puede 
        ver los archivos hacia adelante o hacia atrás
        
        Ejemplo Ruta absoluta:
            Windows: C:\documentos\python\aprendiendo_python\ejemplo_archivo.txt
            Linux: home/usr/local/ejemplo_archivo.txt
        
        Ejemplo Ruta relativa:
            Windows: \python\aprendiendo_python\ejemplo_archivo.txt
            Linux: /local/ejemplo_archivo.txt
            
    La extensión en archivos legibles no importa

    .csv
    .txt
    .tsv
    .json
    .py
    etc
    
    open(arhivo, modo)
    w : escritura. Si no existe, lo crea; si existe, lo reemplaza
    a : crea el fichero si no existe; si existe, agrega nuevo contenido
    r : lectura del archivo
    x : modo de escritura para crear un nuevo archivo. En caso de que el archivo exista 
        se emitirá un error de tipo
    wb: escritura en binario
    rb: lectura en binario
    + : es un modo de escritura/lectura
    
    Nota: si utilizamos el open solito (sin el with) nosotros seremos los 
    encargados de controlar todos los estados del archivo, ej:

    cerrar el archivo: nombre_archivo.close()
    cerrar el archivo el caso de excepciones:  try/finally ó try/except
    # Mala práctica
    open(archivo, modo)
    try
        open(archivo, modo)
        # Lógica de archivos
    finally archivo.close()

    # Buena practiva
    with open(archivo, modo) as soypython:
        lógica de archivos
"""

# readlines | nos devuelve cada fila del archivo en una lista
with open("E:\polisura\python\ejemplo_archivo_2.txt", "r") as archivo:
    contenido = archivo.readlines()
    print(f"Lista: {contenido}, elementos son: {len(contenido)}")
    print("*" * 50)
    for linea in contenido:
        texto = linea.replace("\n", "")
        print(texto)
        #print(f" valor : {texto}")
    print("*" * 50)
    for linea, texto in enumerate(contenido):
        texto = texto.replace("\n", "")
        print(f"el # de la línea es: {linea + 1}, valor : {texto}")

# read | Nos entrega caracter por caracter
with open("ejemplo_archivo.txt", "r") as contenido:
    contenido = contenido.read()
    for linea in contenido:
        print(f"-- {linea}")


# readline | Ejecución perezosa. Ejecuto y llamo una línea del archivo 
# cuando la necesite
print("*" * 50)
with open("ejemplo_archivo.txt", "r") as contenido:
    print(contenido.readline())
    print(contenido.readline())
    print(contenido.readline())

# read | para escribir en el archivo

with open("ejemplo_archivo.txt", "w") as archivo:
    archivo.write("Esto es una línea nueva\n")
    archivo.write("Esto es otra línea nueva\n")
    archivo.write("Esto es la última línea nueva\n")

# write modo append | para añadir contenido al final del archivo
with open("ejemplo_archivo.txt", "a") as cualquier_alias:
    cualquier_alias.write("clase #8\n")
    cualquier_alias.write("[1,2,3,4, True]")

# write modo seek | se utiliza para cambiar la posición del puntero dentro 
# de un archivo. Esto permite moverse a diferentes partes del archivo para 
# leer o escribir datos en ubicaciones específicas.

with open("ejemplo_archivo_2.txt", "w") as cualquier_alias:
    # indicar dónde está el cursor
    print(cualquier_alias.tell())
    print(cualquier_alias.seek(0, 0))
    cualquier_alias.write("profe, me quiero morir \n")
    print(cualquier_alias.tell())

