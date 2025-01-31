"""Varias de las diferentes afunciones globales que tiene Python"""
#Print
print("Hola, mundo!")
#Type
print(type("hola, mundo!"))
#Input
#algo: str = input("ingrese un valor: ")
#print(algo)
#Abs
print(abs(-5))
#Round
print("Redondeo:", round(3.14159))
"""nos permite indicar cuanto decimales para el redondeo"""
print("Redondeo:", round(3.14159, 2))
#Len
print(len([1, 2, 3]))
print(len("abcd"))
#Sum
print(sum([1, 2, 3, 4, 5]))
#Max
print(max([1, 2, 3, 4, 5]))
#Min
print(min([1, 2, 3, 4, 5]))
#Range (range(inicial, final, salteo))
# forma 1
rango = range(5)
print(rango)
print(list(rango))
# forma 2
rango = range(2,5)
print(list(rango))
# forma 3
rango = range(0,11,2)
print(list(rango))
#Sorted
print(sorted([2, 1, 3, 5, 4]))
#Chr
ascii_val = 65
print(chr(ascii_val))
ascii_val = 64
print(chr(ascii_val))
#Ord
print(ord('A'))
print(ord('@'))
#Pow
print(pow(2, 2))
print(pow(9, 3))
#Enumerate
lista = [2, 1, 3, 5, 4]
lista_enumerados = enumerate(lista)
print(lista_enumerados)
print(list(lista_enumerados))
#Con letras
lista_enumerados = enumerate("abcdefgh")
print(lista_enumerados)
print(list(lista_enumerados))
#Cambiando la posición
lista_enumerados = enumerate("abcdefgh", 1)
print(lista_enumerados)
print(list(lista_enumerados))
#Hash
print(hash("a"))
print(hash("a"))
print(hash((1,2,3)))
#Zip
nombres = ["Ana", "Juan", "María", "Luis"]
edades = [25, 30, 28]
combinados = zip(nombres, edades)
print(combinados)
print(list(combinados))
combinados = zip(edades, "abc")
print(list(combinados))
#Any
print(any([False, True, False]))
#All
print(all([True, True, True]))
print(all([True, True, False]))
#DiviMod
print(divmod(5, 2))
print(5 % 2 == 0)
#Reversed
print(reversed([1, 2, 3, 4]))
print(list(reversed([1, 2, 3, 4])))
"""Reversed con slices"""
print([1, 2, 3, 4][::-1])
