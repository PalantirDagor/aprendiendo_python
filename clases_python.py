"""
    TERMINOLOGÍA Clases
    Descripción general de la terminología de programación orientada a objetos

    Método: un tipo especial de función que se define en una definición de clase.

    Variable de clase o atributo: una variable compartida por todas las instancias 
    de una clase. Las variables de clase se definen dentro de una clase pero fuera de 
    cualquiera de los métodos de la clase. Las variables de clase no se utilizan con 
    tanta frecuencia como las variables de instancia.

    Clase: un prototipo definido por el usuario para un objeto que define un conjunto 
    de atributos que caracterizan cualquier objeto de la clase. Los atributos son 
    miembros de datos (variables de clase y variables de instancia) y métodos, 
    a los que se accede mediante notación de puntos.

    Miembro de datos: una variable de clase o variable de instancia que contiene datos 
    asociados con una clase y sus objetos.

    Sobrecarga de funciones: la asignación de más de un comportamiento a una función 
    particular. La operación realizada varía según los tipos de objetos o argumentos 
    involucrados.

    Variable de instancia: una variable que se define dentro de un método y pertenece 
    solo a la instancia actual de una clase.

    Herencia - La transferencia de las características de una clase a otras clases 
    que se derivan de ella.

    Instancia : un objeto individual de una determinada clase. Un objeto obj que 
    pertenece a una clase Círculo, por ejemplo, es una instancia de la clase Círculo.

    Instanciación: la creación de una instancia de una clase.
    
    CONCEPTOS BÁSICOS
    Buenas prácticas:

    Las clases siempre empiezan en mayúscula, y si hay palabras compuestas, se usa 
    camel case

    La instancia de la clase siempre se llama como el objeto, pero la primera 
    letra se coloca en minúscula

    PersonaNatural
    
    personaNatual = PersonaNatual
"""
# objeto vacío
class MiPrimeraClase:
    pass

# instancia | objeto en mem para acceder a atrb y meth
miPrimeraClase = MiPrimeraClase()
curso = MiPrimeraClase()
print(curso)

print("*" * 50)
# analizando el objeto
print(MiPrimeraClase)
print(miPrimeraClase)
print(type(miPrimeraClase))
print(id(miPrimeraClase))
print(hex(id(miPrimeraClase)))

print(type(curso))
print(MiPrimeraClase.__name__) # obtiene la clase sin instancia
print(curso.__class__) # obtiene la clase padre con clase sin instancia
#print(curso.__name__)

"""
    DIR
    Listar los atributos y métodos de un objeto

    Tip: muchas cosas en las clases de Python se manejan con diccionarios
"""
print("*" * 50)
longitud_a = len(dir(MiPrimeraClase)) # cuantas funciones o atributos tiene la clase
print(longitud_a)
print(dir(MiPrimeraClase))
print("*" * 50)
longitud_b = len(dir(MiPrimeraClase))
print(longitud_b)
print(dir(miPrimeraClase))

"""
    CONCEPTOS BÁSICOS + 1
    
    Siempre para garantizar que una función pertenece a la instancia de la clase, 
    debe tener la palabra self

    cuando definan una metodo(función) siempre el primer argumento es self

    self --> se está apuntando a sí mismo
"""

def saludar(nombre: str) -> None:
  print(f"holaaaa {nombre}")

saludar("spartan@s de nivel 2")

class CursoBackend:
    nivel: int = 2
    tema: str = "Python"
    desc: str = "entrenamiento intensivo"

    # es un apuntador en memoria
    def saludar(self, nombre: str) -> None:
        print(f"holaaaa {nombre}")

    # no siempre se llama self, pero es usado internacionalmente
    def saludar_2(mangano, nombre: str) -> None:
        print(f"holaaaa que mas {nombre}")

cursoBackend = CursoBackend()
print(cursoBackend)
# accediendo
print(cursoBackend.tema)

# modificar
CursoBackend.tema = "Python viendo POO y PF"
print(CursoBackend.tema)

print(cursoBackend.saludar("Queridos alumnos del curso!!"))
print(cursoBackend.saludar_2("para todos los nuevos!!"))
print("*" * 50)
# print(CursoBackend.saludar(nombre="Queridos alumnos del curso!!"))
# print(CursoBackend.saludar_2(nombre="para todos los nuevos!!"))

""" Clases Nivel 1"""

class Program:
    # variables públicas | spoiler
    language = "Python"
    version = "3.11"

    def hello(self):
        print(f"Hello OOP with : {Program.language}")

programa = Program()
print(programa.version)
print(programa.hello())
programa.hello()

"""
    GETATTR
    get - obtener
"""
print("*" * 50)
print(Program.version)
print(getattr(Program, "language"))
print(getattr(programa, "version"))

"""
    SETATTR
    SET - asignar o configurar
"""
print("*" * 50)
# inyectando al padre
print(dir(Program))
setattr(Program, "id", 12345)
print(dir(Program))
print("*" * 50)
# inyectando instancia
setattr(programa, "id_2", 895623)
print(f"clase Original: {dir(Program)}")
print(f"instancia de clase: {dir(programa)}")
"""
    DELATTR
    DELETE - borrar
"""
print("*" * 50)
delattr(Program, "id")
delattr(programa, "id_2")
print(f"clase Original: {dir(Program)}")
print(f"instancia de clase: {dir(programa)}")

""" 
    METADATA BÁSICA
    DATOS DE CLASE
    NOTA IMPORTANTE:

    La mayoría de los atributos y métodos están almacenados en una clase y se manejan como un diccionario

    usando __dict__ no podemos setear objetos directamente a la clase
"""
# __dict__
print("*" * 50)
print(Program.__dict__)
# acceder a los datos
print(Program.__dict__["language"])
# no se asigna como en diccionarios, saca error
# Program.__dict__["language"] = "Java"
# Program.__dict__["hello"]()

## Usando instalcias de la clase Program
el_apuntador = Program()
print(f" programa     : {id(programa)}")
print(f" el_apuntador : {id(el_apuntador)}")
Program.__dict__["hello"](programa)
Program.__dict__["hello"](el_apuntador)

"""
    ATRIBUTOS
    Inicio de la teoría de encapsulamiento. El encapsulamiento es débil en Python

    pública: si no tienen nada adelante, es una variable pública
    _semi_pública: si tiene un guion `_` adelante se conoce como semi pública
    __privada: si tiene dos guiones de piso `__` es privada (teóricamente, pero no es del todo cierto)
    Nota: estos nombres aplican tanto para métodos como para atributos
"""
class AccountBank:
    bank: str = "CursoBackend"
    _level: int = 3
    __taxes: float = 0.34
# una variable privada es para trabarla únicamente en la clase
# las variables públicas y semi se pueden trabajar dentro de la clase o fuera
print("*" * 50)
accounBanc = AccountBank()
print(accounBanc.bank)
print(accounBanc._level)
print(accounBanc.__taxes)
