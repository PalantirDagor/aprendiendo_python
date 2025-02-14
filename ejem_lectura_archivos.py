
with open("ejemplo_archivo.txt", "a") as archivo:
   #contenido: str = archivo.read()
   #print("Contenido archivo: "#, contenido)
   #print(#contenido.upper())
   #print(contenido.count("Python"))
   print(archivo.tell())
   print(archivo.seek(24, 0))
   print(archivo.tell())
   archivo.write("profe, me quiero morir \n")



