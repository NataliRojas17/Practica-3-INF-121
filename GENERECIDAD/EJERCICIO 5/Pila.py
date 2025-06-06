from typing import TypeVar, Generic, List

T = TypeVar('T')
class Pila(Generic[T]):
    def __init__(self):
        self.elementos: List[T] = []
    def apilar(self, elemento: T):
        self.elementos.append(elemento)
    def desapilar(self) -> T | None:
        if len(self.elementos) > 0:
            return self.elementos.pop()
        else:
            return None
    def mostrar_pila(self):
        print("Contenido de la pila:")
        for elemento in reversed(self.elementos):
            print(elemento)
            
pila_enteros = Pila[int]()
pila_enteros.apilar(10)
pila_enteros.apilar(20)
pila_enteros.apilar(30)
pila_enteros.apilar(40)
pila_enteros.apilar(50)

print("Pila de enteros")
print("-" * 18)
pila_enteros.mostrar_pila()

print("Desapilando ---> ", pila_enteros.desapilar())
pila_enteros.mostrar_pila()
pila_cadenas = Pila[str]()
pila_cadenas.apilar("Buenos dias")
pila_cadenas.apilar("Buenas tardes")
pila_cadenas.apilar("Buenas noches")

print("\nPila de cadenas")
print("-" * 18)
pila_cadenas.mostrar_pila()
print("Desapilando ---> ", pila_cadenas.desapilar())
pila_cadenas.mostrar_pila()
