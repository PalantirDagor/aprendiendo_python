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
"""Ejemplo: valor_si_cumple if condicion else valor_si_no_cumple"""
lista_documento: list = ["CC", "NIT", "CE", "PASP"]
# forma comprimida
# valor_si_cumple if condicion else valor_si_no_cumple
print(True if len(lista_documento) == 4 else False)
# forma stringas
# valor_si_cumple if condicion else valor_si_no_cumple
lista_valida = "YES" if len(lista_documento) == 4 else "NO"
lista_valida

#Pass
# aquí validaré x cosa
if 1 == 1:
    # no implementación
    pass

"""
    Estructura condicional Match
    Solo es válido a partir de la versión 3.10 de Python
    match dato:
        case condicion:
            # logica
        case n:
            # ...
            
    Validaciones como el if
    Me permite trabajar con iterables haciendo desacoplamiento
    Me permite aplicar condicionales comprimidos
"""

tipo_doc: str = input("por favor ingrese el documento, valores permitidos: \n" + "\n".join(lista_documento))
# documento_valido : bandera lógica | ESTUDIAR

documento_valido: bool = False
match tipo_doc:
  case "CC":
    documento_valido = True
  case "NIT":
    documento_valido = True
  case "CE":
    documento_valido = True
  case"PASP":
    documento_valido = True
  case _:
    # documento_valido = False
    print("el dato ingresado por el usuario es inválido")
    print(f"valor ingresado {tipo_doc}, valores permitidos: {lista_documento}")

if documento_valido:
  print("¡Yupii! El dato ingresado por el usuario es válido")

