from typing import Generic, TypeVar, List

T = TypeVar('T')
class Catalogo(Generic[T]):
    def __init__(self):
        self.elementos: List[T] = []

    def agregar_elemento(self, elemento: T):
        self.elementos.append(elemento)

    def buscar_elemento(self, indice: int) -> T | None:
        if 0 <= indice < len(self.elementos):
            return self.elementos[indice]
        else:
            return None

    def mostrar_elementos(self):
        for elemento in self.elementos:
            print(elemento)
class Libro:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"Libro: {self.titulo} - Autor: {self.autor}"

catalogo_libros = Catalogo[Libro]()
catalogo_libros.agregar_elemento(Libro("Bajo la misma estrella ", "John Green"))
catalogo_libros.agregar_elemento(Libro("Maravilloso desastre", "Jamie McGuire"))

print("Catálogo de Libros:")
catalogo_libros.mostrar_elementos()

