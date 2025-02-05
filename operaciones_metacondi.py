"""
    Metacondiciones, Operadores logicos y operadores matematicos
    en Python y sus usos!!
"""
"""Metacondiciones"""
num_a: int = 1
num_b: int = 2

# mayor
print("num_a: " + str(num_a) + " > " + "num_b: " + str(num_b))
print(num_a > num_b)

# menor
print("num_a: " + str(num_a) + " < " + "num_b: " + str(num_b))
print(num_a < num_b)

# menor o igual
print("num_a: " + str(num_a) + " <= " + "num_b: " + str(num_b))
print(num_a <= num_b)

# mayor o igual
print("num_a: " + str(num_a) + " >= " + "num_b: " + str(num_b))
print(num_a >= num_b)

# diferente
print("num_a: " + str(num_a) + " != " + "num_b: " + str(num_b))
print(num_a != num_b)

# comparación
print("num_a: " + str(num_a) + " == " + "num_b: " + str(num_b))
print(num_a == num_b)

"""
    Operadores lógicos
    and       AND lógico
    or        OR  lógico
    not       Negación
    
         x      y  (x OR y)  (x AND y)
        ----------------------------------
        True   True    True      True
        True   False   True      False
        False  True    True      False
        False  False  False      False
"""
num_1: int = 1
num_2: int = 5
num_3: int = 2
num_4: float = 3.5

# or
print("num_1: " + str(num_1), "num_2: " + str(num_b), "num_3: " + str(num_3), "num_4: " + str(num_4))
print(num_1 > num_2 or num_3 < num_4)

# and
print("num_1: " + str(num_1), "num_2: " + str(num_b), "num_3: " + str(num_3), "num_4: " + str(num_4))
print(num_1 > num_2 and num_3 < num_4)

# not
print("sin 'not'")
print(1 > 2)
print("utilizando 'not'")
print(not 1 > 2)

"""
    Operador 'in'
    Validar si algún elemento está en el otro
    Aplica principalmente para iterables
"""
curso: str = "curso de backend con Python"
print("utilizando 'in'")
print("Python" in curso)

""" 
    Operadores Matematicos
    Orden de operaciones matemáticas:

    Paréntesis
    Exponente
    Multiplicación
    División
    Suma
    Resta
    Nota: las operaciones de multiplicación y división se realiza de 
    izquierda a derecha ejemplo: 7 + (6 × 5^2 + 3 + (1+1 + (2+2)))

    problema: 7 + (6 × 5^2 + 3)

    (6 × 5^2 + 3)
    (6 × 25 + 3)
    (150 + 3)
    (153)
    7 + (153)
    R == 160
    ejemplo_2: valor a: 1, valor b: 5, valor c: 2, valor d: 3.5

    (a > b) and (c < d)

    (a > b) = False
    (a > b) = True False True = False
"""
# suma
print(num_a + num_b + num_1)

# resta
print(num_a - num_b)

# multiplicación
print(num_a * num_b)

# division normal
print(num_b/num_a)

# division entera
print(num_a // num_b)

# exponencial
print(num_2 ** num_b)

# Modulo
print(num_a % num_b)
print(4 % num_b)
