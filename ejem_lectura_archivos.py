
with open("ejemplo_archivo.txt", "r") as archivo:
   contenido: str = archivo.read()
   print("Contenido archivo: ", contenido)
   print(contenido.upper())
   print(contenido.count("Python"))
   

