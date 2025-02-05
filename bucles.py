"""
    Bucles o estrucuruas de repeticion for y while
"""
"""
    Ciclo for
    Ciclo controlado (mejor amigo para recorrer)

        for una_o_varias_variables_temporales in iterable (en memoria | calculado): [obligatoria]
            pass o la lógica que quieran
        else: [opcional]
"""
# for simple

texto: str = "curso.de.backend.con.Python"

for letra in texto:
  print(letra, letra * 5)

print("-------------------------------")
# for con else
# curso
# for letra in texto[0:8]:
for letra in texto.split(".")[0]:
  print(letra, letra * 5)
else:
  print("finalizó!")
  
# lista = ["curso", "de", "backend", "con", "Python"]
# "curso" = lista[0]

# for con continue (Sirve tanto para for como para while)
for letra in texto:
  if letra == ".":
    print(letra, letra * 5)
  else:
    continue
print("---------------------------------")
for letra in texto:
  
  if letra == ".":
    continue
  print(letra, letra * 5)
  
  print("usando pass dentro del if")
  for letra in texto:
    if letra == ".":
        pass
    print(letra, letra * 5)

# for con break (Sirve tanto para for como para while)
print(texto)
print(len(texto))

for letra in texto:
  if letra == ".":
    break
  print(letra, letra * 5)
else:
  print("ejecutando el else!")

print("continúa ejecutando las líneas siguientes...")

# for anidados (Nota: aplica para if, para bucles y para funciones)

# Multiplicación
for numero_1 in range(1,11):
  # Al nivel de indentación del bucle | break o continue se ponen donde quiere que se rompa u omita
  for numero_2 in range(1,11):
    #if ..:
      # lógica
    print(f"{numero_1} x {numero_2} = {numero_1 * numero_2}")
    
"""
    for comprehension
    Siempre devolverá una lista
    Permite for anidados
    [ acciones for temporal in iterable condiciones]
    Cómo abordar un for comprimido

    Especificar el código de iteración
    Especificar las acciones
"""
# simple
resultado = [ letra * 5 for letra in texto ]
# resultado = [ (letra, letra * 5) for letra in texto]
print(resultado)

# for comprehension con if
print("---------------------------------------")
resultado_2 = [ (letra, letra * 5) for letra in texto[:10] if letra != "."]
print(resultado_2)

# for comprehension anidado
resultado_3 = [ f"{numero_1} x {numero_2} = {numero_1 * numero_2}" for numero_1 in range(1,11) for numero_2 in range(1,11)]
print(resultado_3)

# Ciclo for usado para iterar un diccionario
print("---------------------------------------")
dicc: dict = {
    "nombre": "Pepito",
    "apellido": "Pérez",
    "edad": 1, "sangre": {
        "rh": "+", "grupo": "AB"
    }
}

for llave, valor in dicc.items():
  print(f"La llave se llama |{llave}|, y el valor de la llave es: |{valor}|")

"""
    Ciclo while
    Funciona iterando hasta que se cumpla una condición

    CUIDADO! Es un ciclo no controlado, es decir que usted debe indicar cuándo termina

        while condicion: [obligatoria]
            pass o la logica que quieran
        else: [opcional]
"""
print("--------- Ciclo while -----------")
rango: int = 5
contador: int = 0

while contador < rango:
  print(contador)
  #contador = contador + 1
  contador += 1
else:
  print("finalizó!")
