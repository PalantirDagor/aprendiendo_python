"""
    Pilares de POO (Programación Orientada o Objetos)
    Encapsulamento, Herencia, Polimorfismo y Abstracción
"""
class AccountBank:
  bank: str = "CursoBackend"
  _level: int = 2
  __taxes: float = 0.34

accounBank = AccountBank()
print(accounBank.bank)
print(accounBank._level)
# Error por el encapsulamiento, variable privada
# print(accounBank.__taxes)

""" 
    Herencia
    
    La herencia permite que una clase (llamada clase derivada o subclase) herede atributos y métodos de otra clase (llamada clase base o superclase). Principalmente se usa para:

    -Reutilización de código
    -Programación avanzada
    -Polimorfismo (lo veremos más adelante): El polimorfismo se basa en la herencia 
        y la capacidad de las clases derivadas de una clase base para sobrescribir 
        (anular) sus métodos. Esto permite que el mismo método o función pueda comportarse 
        de manera diferente según el tipo de objeto con el que se esté trabajando, lo que 
        aporta versatilidad y extensibilidad al código.
    -heredar estado y comportamiento
    Nota: cuando creamos una clase heredamos implícitamente de object

    class NombreClase(ClaseHeredar1, ClaseHeredar2, ClaseHeredar ....... n):
        pass
"""
class Persona:
    id: str = "NIDF"
    nombre: str = ""
    edad: int = ""    
    def __init__(self, genero: str = "NO_IMPORTA"):
        self.__gen = genero
    
    def dormir(self):
        print(f"la persona con edad {self.edad} debe dormir x horas al día")

    def _genero_para_curso(self):
        print(f"preferencia de género para el curso: {self.__gen} ")

# no requerido, redundante | se hacia en python 2, pero en versiones modernas no requerido
# class Persona(object):
#    pass
print("*" * 50)
# Herencia elemental o simple en Python
class Profesor(Persona):
    def calcular_salario(self, horas_trabajadas: int, valor_horas: int):
        return horas_trabajadas * valor_horas

profesor = Profesor()
print(profesor.id)
profesor.id = "12345"
print(profesor.id)
profesor.dormir()
print(profesor.calcular_salario(10, 10000))

# Herencia Múltiple en Python
class GeneradorIdentificadores:
    def obtener_hash_persona(self, id: str = "ND", nombre: str = "ND", edad: int = 0):
        print(id)
        print(nombre)
        print(edad)
        return hash((
            "id",id,
            "nombre", nombre,
            "edad", edad))

class Profesor(Persona, GeneradorIdentificadores):
    def calcular_salario(self, horas_trabajadas: int, valor_horas: int):
        return horas_trabajadas * valor_horas

profesor = Profesor()
print(dir(profesor))

"""
    Polimorfismo
    El polimorfismo se basa en la herencia y la capacidad de las clases derivadas 
    de una clase base para sobrescribir (anular) sus métodos. Esto permite que el 
    mismo método o función pueda comportarse de manera diferente según el tipo de 
    objeto con el que se esté trabajando, lo que aporta versatilidad y extensibilidad 
    al código.
"""
class Animal:
    rama: str = "biología & taxonomía"
    def comunicacion(self, defecto: str = "hablar") -> str:
        return defecto

    def comunicacion_mala_practica(self, defecto):
        return defecto

class Perro(Animal):
    def comunicacion(self) -> None:
        print("Woof!")

class Gato(Animal):
    def comunicacion(self) -> None:
        print("Meow!" * 10)

class Humano(Animal):
    rama: str = "desconocida"
    pass

print("*" * 50)
# analicemos animal
animal = Animal()
print(type(animal.comunicacion))
print(animal.comunicacion.__name__)
print(animal.comunicacion.__annotations__)
print(animal.comunicacion_mala_practica.__annotations__)
valor = animal.comunicacion()
funcion = animal.comunicacion
print(valor)
print(funcion())

print("*" * 50)
# analicemos animal
perro = Perro()
print(type(perro.comunicacion))
print(perro.comunicacion.__name__)
print(perro.comunicacion.__annotations__)
print(perro.comunicacion_mala_practica.__annotations__)
valor = perro.comunicacion()
funcion = perro.comunicacion
print(valor)
funcion()

print("*" * 50)
# analicemos gato
gato = Gato()
gato.comunicacion()
print(gato.rama)
print("*" * 50)
humano = Humano()
print(humano.rama)
print(humano.comunicacion())
print(humano.comunicacion.__annotations__)

"""
    Abstracción
    La abstracción es el concepto de ocultar ciertas características y comportamientos 
    de una clase y proporcionar una interfaz común para interactuar con ella. Esto 
    permite que las clases derivadas puedan implementar sus propias características y 
    comportamientos, manteniendo una estructura unificada y evitando la redundancia.
    
    Unas clases en las que se pueden definir tanto métodos como propiedades, pero que no 
    pueden ser instancias directamente. Solamente se pueden usar para construir subclases. 
    Permitiendo así tener una única implementación de los métodos compartidos, evitando 
    la duplicación de código.
    
    Notas:

    Los métodos abstractos pueden tener o no lógica
    siempre se debe usar abstractmethod (es su amigo, su aliado, su pana)
"""

from abc import ABC, abstractmethod

# está mal - no se puede instanciar directamente
#class Animal(ABC):
#    def mover(self):
#        pass

#animal = Animal()

class Animal(ABC):
    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def comer(self, alimento: str) -> str:
        pass

# Error no se puede instanciar la clase por ser abstracta
# animal = Animal()
print("*" * 50)
class Gato(Animal):
    duerme: str = "día"
    def mover(self):
        print("ágilmente")

    def comer(self, preferido: str, alternativos: list) -> None:
        print(preferido)
        print(alternativos)
    
    def comunicacion(self) -> None:
        print("Meow!" * 10)

gato = Gato()
print(gato.duerme)
gato.mover()
gato.comer("pollo", ["mirringo", "atuncito"])
gato.comunicacion()
