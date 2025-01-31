"""
    Sets y sus metodos  y la manera de utilizarlos
"""
valor: set = {1,2,3,1}
print(valor, type(valor))

"""Operaciones generales con los Sets"""
# Permite tener conjuntos de un solo tipo o mixtos
set_numericos = {1,2,3}
set_letras ={"a","b","c"}
set_mixto = {"a",1,3.15}

print("Numéricos -> tipo de dato : {}, valor : {}".format(type(set_numericos),set_numericos))
print("Texto     -> tipo de dato : {}, valor : {}".format(type(set_letras),set_letras))
print("Mixto     -> tipo de dato : {}, valor : {}".format(type(set_mixto),set_mixto))

"""Metodo Append (.add): sirve para ingresar datos al set"""
elementos: int = {1,2}
print(elementos)
elementos.add(3) # similar al append en listas
print(elementos)

"""Metodo Update: nos actualiza nuestro set con nueva data"""
print(elementos)
elementos.update([1,2,3,"b", (1,2)])
print(elementos)

"""Metodo Discart: Nos elimina el elemento que le pasamos por parametro y 
que este dentro del Set"""
print("Antes: ", elementos)
elementos.discard(1)
print("Despues: ", elementos)
#No esta el elemento
elementos.discard(4)
print("No elemento 4: ", elementos)

"""Metodo Remove: """
print("Antes: ", elementos)
elementos.remove(2)
print("Despues: ", elementos)
#No esta el elemento
#elementos.remove(4)
print("No elemento 4: ", elementos)

"""Metodo Pop: """
print("Antes: ", elementos)
elementos.pop()
print("Despues: ", elementos)

"""
OPERACIONES BÁSICAS DE CONJUNTOS
Estas operaciones, se pueden trabajar:

por operador
por función
Nota: No es implicito, el valor resultante se debe almacenar en una 
variable, en caso de que la quiera persistir
"""

#Union
set_a = {1,2,3,4,5,6}
set_b = {4,5,6,7,8,9}

print("1. forma con operador --> ", set_a | set_b)
print("2. forma con función  --> ", set_a.union(set_b))
print("3. forma con función  --> ", set_b.union(set_a))

set_a = {1,2,3,4,5,6}
set_b = {4,5,6,7,8,9}
set_c = {8,9,10,11}

print("1. forma con operador --> ", set_a | set_b | set_c )
print("2. forma con función  --> ", set_a.union(set_b).union(set_c))
print("3. forma con función  --> ", set_b.union(set_a).union(set_c))

#INTERSECCIÓN
print("1. forma con operador --> ", set_a & set_b)
print("2. forma con función  --> ", set_a.intersection(set_b))
print("3. forma con función  --> ", set_b.intersection(set_a))

#DIFERENCIA
print("1. forma con operador --> ", set_a - set_b)
print("2. forma con función  --> ", set_a.difference(set_b))
print("3. forma con función  --> ", set_b.difference(set_a))

#DIFERENCIA SIMÉTRICA
print("1. forma con operador --> ", set_a ^ set_b)
print("2. forma con función  --> ", set_a.symmetric_difference(set_b))
print("3. forma con función  --> ", set_b.symmetric_difference(set_a))

"""
  Problemas:
    1. la base de datos tiene usuarios repetidos
    2. el usuario, realizó mal un sql y el sql está duplicando la información
"""
# Respuesta de negocio: cuántos usuarios registrados tenemos
datos: tuple = ("123", "456", "123", "789", "111", "123") # SQL acceder a las bases de datos
print("Usuarios activos: ", len(datos))

# optimizada
unicos = tuple(set(datos))
print("Usuarios activos: ", len(unicos))
