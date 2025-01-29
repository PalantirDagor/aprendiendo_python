"""
    Numeros y Booleanos, usos y alguno que otro truco
"""

valor1: int = 5
valor2: int = 2

print("suma           : ", valor1 + valor2)
print("resta          : ", valor1 - valor2)
print("multiplicacion : ", valor1 * valor2)
print("division       : ", valor1 / valor2)
print("operaciones    : ", ((valor1 * valor2) + 555) / 35)

resultado_division = valor1 / valor2
print(type(resultado_division), resultado_division)

# True  = 1
# False = 0

es_verdadero: bool = True
es_falso: bool = False
print(es_verdadero, es_falso, type(es_verdadero), type(es_falso))

print(1 + True + False + True)

print("1 es igual a 2?: ", 1 == 2)

