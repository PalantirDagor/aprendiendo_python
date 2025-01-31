"""
    Estructuras condicionales IF
if condicion:     # [1] requerido
  accion
elif condicion:  #  [2] opcionales
  accion
elif condicion:
  accion
else:            #  [3] opcional
  accion
"""
print(1 == 1)

resultado = True

# no realizar, redundante | mala práctica
if resultado == True:
    print("cumplió")

# buenas prácticas
if resultado:
    print("cumplió")

#resultado = False

if resultado:
    print("cumplió")
else:
    print("NO cumplió")

#If Else If "elif"
a : int = 1
b : int = 1

if a == b:
    print("a es igual a: b")
elif a > b:
    print("a es mayor que b")
elif a < b:
    print("a es menor que b")
#IF ELSE IF ELSE
if a > b: # or b == a:
    print("a es mayor que b")
elif a < b:
    print("a es menor que b")
else:
    print("ninguno de los casos corresponde")
#If comprimido
lista_documento: list = ["CC", "NIT", "CE", "PASP"]
print(True if len(lista_documento) == 4 else False)
#Pass
# aquí validaré x cosa
if 1 == 1:
    # no implementación
    pass

