import json
import os

class Cliente:
    def __init__(self, id, nombre, edad, ciudad, celular):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
        self.celular = celular

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "edad": self.edad,
            "ciudad": self.ciudad,
            "celular": self.celular
        }

    @staticmethod
    def from_dict(data):
        return Cliente(
            data["id"],
            data["nombre"],
            data["edad"],
            data["ciudad"],
            data.get("celular", 0)  
        )

class ArchivoCliente:
    def __init__(self, nomA):
        self.nomA = nomA
        self.clientes = []
        self.cargar_desde_archivo()

    def guardar_cliente(self, c):
        if not any(cliente.id == c.id for cliente in self.clientes):
            self.clientes.append(c)
            self.guardar_en_archivo()
        else:
            print(f"Cliente con ID '{c.id}' ya existe. No se agregó de nuevo.")

    def guardar_en_archivo(self):
        with open(self.nomA, "w") as f:
            json.dump([cliente.to_dict() for cliente in self.clientes], f, indent=4)

    def cargar_desde_archivo(self):
        if os.path.exists(self.nomA):
            try:
                with open(self.nomA, "r") as f:
                    data = json.load(f)
                    self.clientes = [Cliente.from_dict(d) for d in data]
            except json.JSONDecodeError:
                self.clientes = []
        else:
            self.clientes = []

    def buscar_cliente(self, nombre):
        for cliente in self.clientes:
            if cliente.nombre.lower() == nombre.lower():
                return cliente
        return None

    def buscar_cliente_por_id(self, id):
        for cliente in self.clientes:
            if cliente.id == id:
                return cliente
        return None

    def buscar_celular_cliente(self, id):
        cliente = self.buscar_cliente_por_id(id)
        if cliente:
            return {
                "id": cliente.id,
                "nombre": cliente.nombre,
                "edad": cliente.edad,
                "ciudad": cliente.ciudad,
                "celular": cliente.celular
            }
        else:
            return None

    def mostrar_clientes_ciudad(self, ciudad):
        encontrados = [c for c in self.clientes if c.ciudad.lower() == ciudad.lower()]
        if encontrados:
            for c in encontrados:
                print(f"{c.nombre}, {c.edad}, {c.ciudad}, {c.celular}")
        else:
            print(f"No hay clientes en la ciudad: {ciudad}")

if __name__ == "__main__":
    archivo = ArchivoCliente("clientes.json")

    archivo.clientes = []
    archivo.guardar_en_archivo()

    archivo.guardar_cliente(Cliente(1, "Natali", 25, "La Paz", 76543210))
    archivo.guardar_cliente(Cliente(2, "Fernando", 30, "Santa Cruz", 71234567))
    archivo.guardar_cliente(Cliente(3, "Eduardo", 40, "La Paz", 79876543))

    buscado = archivo.buscar_cliente("Natali")
    if buscado:
        print(f"Encontrado: {buscado.nombre}, {buscado.ciudad}")
    else:
        print("Cliente no encontrado.")

    print("Clientes en La Paz:")
    archivo.mostrar_clientes_ciudad("La Paz")

    print("\nBuscar cliente por ID 2:")
    cliente_id_2 = archivo.buscar_cliente_por_id(2)
    if cliente_id_2:
        print(f"Cliente ID 2: {cliente_id_2.nombre}, {cliente_id_2.ciudad}")

    print("\nBuscar cliente y celular por ID 3:")
    cliente_celular = archivo.buscar_celular_cliente(3)
    if cliente_celular:
        print(cliente_celular)
    else:
        print("Cliente no encontrado por ID.")
