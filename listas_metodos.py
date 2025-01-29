"""
    Listas y sus metodos
"""

lista_vacia = []
lista_numeros = [1, 2, 3, 4 ,5 ,6, 4]
lista_letras = ["a", "b", "c"]
lista_mix = [1, True, 3.5, [1,2], str.upper, (1,2), "hola!"]

""" Usando el metodo Upper de la lista"""
print(lista_mix[4]("Esto funciona con mayusculas"))

"""Obteniendo el numero de una lista dentro de otra lista"""
print("Obtengo lista: ", lista_mix[3])
print("Obtengo numero: ", lista_mix[3][1])
print("Slices: ", lista_mix[::-1])
print("Slices: ", lista_mix[3][::-1])
print("Slices: ", lista_mix[3:5])
print("Slices: ", lista_mix[3:])
print("Slices: ", lista_mix[:5])

"""Multiplicar los elementos de las listas"""
print(lista_mix[2] * 5)
print(lista_mix[-1] * 5)

"""Listas anidadas"""
valor: str = [1, 2, [[5,6, [7,8]],3,4 ]]
print("paso # 1: ", valor[2])
print("paso # 2: ", valor[2][0])
print("paso # 3: ", valor[2][0][2])
print("paso # 4: ", valor[2][0][2][1])

"""Metodo Append: nos ingresa nuevos elementos a la lista en la ultima posición"""
lista_vacia.append(1)
print(lista_vacia)

lista_vacia.append("Santiago")
print(lista_vacia)

"""Metodo Insert: nos permite ingresar otro elemento a la lista pero en 
la posicion deseada ejemplo: '.insert(indice, valor)'"""
lista_vacia.insert(0, 10)
print(lista_vacia)

lista_vacia.insert(2, "Duvan")
print(lista_vacia)

"""Metodo Remove: eliminar un elemento de la lista, que yo indique"""
lista_vacia.remove(1)
print(lista_vacia)

"""Metodo Pop: elimina el ultimo elemento si no se especifica con un indice"""
lista_vacia.pop()
print(lista_vacia)

lista_vacia.insert(1,"El profe")
print(lista_vacia)

lista_vacia.pop(1)
print(lista_vacia)

"""Metodo Index: me permite buscar un objeto y si lo encuentra, 
me devuelve su posición"""
print("Posicion del elemento a buscar: ")
print(lista_mix.index(3.5))
"""Cuando el valor no esta"""
print("Posicion del elemento a buscar: ")
#print(lista_mix.index("Alumnos"))

"""Metodo Count: nos permite contar las ocurrencas de un objeto en particular"""
print("¿cuantos #4 hay?: ", lista_numeros.count(4))
"""cuando no hay objetos"""
print(lista_numeros.count("Python"))

"""Metodo Sort: nos permite organizar de manera secuencial nuestra lista"""
resultado: list = [3, 1, 2]
print(resultado)
resultado.sort()
print(resultado)

"""Metodo Reverse: nos revierte los elementos de la lista"""
#print(lista_numeros[::-1])
lista_numeros.reverse()
print(lista_numeros)
lista_numeros.sort()
print(lista_numeros)

"""Metodo Clear: nos borra todos los elementos de la lista"""
print(lista_vacia)
lista_vacia.clear()
print(lista_vacia)

"""Metodo Copy: nos genera una copia de la lista original"""
# cs_lista_numeros = lista_numeros
cs_lista_numeros: list = lista_numeros.copy() # esta es la recomendada
cs_lista_letras: list = lista_letras.copy()
print(cs_lista_numeros)
print(cs_lista_letras)

"""Metodo Extend: nos permite extender nuestra lista con otra o concatenar varias listas"""
print(lista_numeros)
lista_numeros.extend(lista_letras)
print(lista_numeros)

"""Modificar valores en las listas"""
print(cs_lista_numeros)
cs_lista_numeros[0] = "zero to hero"
print(cs_lista_numeros)

"""Modificar por rango"""
print(cs_lista_letras)
cs_lista_letras[0:] = ["la A", "la B", "la C"]
print(cs_lista_letras)

"""Desacoplamiento o mapeo de valores"""
lista_desacople: list = "curso.de.bakcend.con.python".split(".")
print(lista_desacople)
print(len(lista_desacople))
