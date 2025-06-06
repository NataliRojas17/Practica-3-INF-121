from typing import TypeVar, Generic

T = TypeVar('T')

class Caja(Generic[T]):
    def __init__(self):
        self.contenido: T = None

    def guardar(self, dato: T):
        self.contenido = dato

    def obtener(self) -> T:
        return self.contenido

caja_texto = Caja[str]()
caja_texto.guardar("Herramientas")

caja_numero = Caja[int]()
caja_numero.guardar(25)

print("Contenido de la caja 1:", caja_texto.obtener())
print("Cantidad de objetos que lleva la caja 2:", caja_numero.obtener())
