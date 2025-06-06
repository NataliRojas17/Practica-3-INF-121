import json

class Medicamento:
    def __init__(self, nombre, codigo, tipo, precio):
        self.nombre = nombre
        self.codigo = codigo
        self.tipo = tipo
        self.precio = precio

    def a_dict(self):
        return {
            "nombre": self.nombre,
            "codigo": self.codigo,
            "tipo": self.tipo,
            "precio": self.precio
        }

    @staticmethod
    def desde_dict(data):
        return Medicamento(data["nombre"], data["codigo"], data["tipo"], data["precio"])

class Farmacia:
    def __init__(self, nombre, sucursal, direccion):
        self.nombre = nombre
        self.sucursal = sucursal
        self.direccion = direccion
        self.medicamentos = []

    def agregar(self, m):
        self.medicamentos.append(m)

    def a_dict(self):
        return {
            "nombre": self.nombre,
            "sucursal": self.sucursal,
            "direccion": self.direccion,
            "medicamentos": [m.a_dict() for m in self.medicamentos]
        }

    @staticmethod
    def desde_dict(data):
        f = Farmacia(data["nombre"], data["sucursal"], data["direccion"])
        for m in data.get("medicamentos", []):
            f.agregar(Medicamento.desde_dict(m))
        return f

    def mostrar_medicamentos_para_tos(self):
        encontrados = [m for m in self.medicamentos if m.tipo.lower() == "tos"]
        if encontrados:
            print(f"Medicamentos para tos en sucursal {self.sucursal}:")
            for m in encontrados:
                print(f"  {m.nombre} - Precio: {m.precio}")
        else:
            print(f"No hay medicamentos para tos en la sucursal {self.sucursal}.")

    def tiene_medicamento(self, nombre_medicamento):
        return any(m.nombre.lower() == nombre_medicamento.lower() for m in self.medicamentos)

class ArchFarmacia:
    def __init__(self, archivo):
        self.archivo = archivo
        self.farmacias = []

    def agregar(self, f):
        self.farmacias.append(f)

    def guardar(self):
        with open(self.archivo, "w") as f:
            json.dump([fa.a_dict() for fa in self.farmacias], f, indent=2)

    def cargar(self):
        try:
            with open(self.archivo, "r") as f:
                data = json.load(f)
                self.farmacias = [Farmacia.desde_dict(fa) for fa in data]
        except FileNotFoundError:
            self.farmacias = []

    def mostrar_todo(self):
        for f in self.farmacias:
            print(f"{f.nombre} - Sucursal {f.sucursal} - Dirección: {f.direccion}")
            for m in f.medicamentos:
                print(f"  {m.nombre} ({m.tipo}) - Precio: {m.precio}")
            print()

    def mostrar_medicamentos_para_tos_sucursal(self, sucursal):
        for f in self.farmacias:
            if f.sucursal == sucursal:
                f.mostrar_medicamentos_para_tos()
                return
        print(f"No se encontró la sucursal {sucursal}")

    def mostrar_sucursales_con_medicamento(self, nombre_medicamento):
        encontrados = False
        for f in self.farmacias:
            if f.tiene_medicamento(nombre_medicamento):
                print(f"Sucursal: {f.sucursal}, Dirección: {f.direccion}")
                encontrados = True
        if not encontrados:
            print(f"No se encontró el medicamento \"{nombre_medicamento}\" en ninguna sucursal.")

archivo = ArchFarmacia("farmacias.json")
archivo.cargar()
archivo.farmacias.clear()

f1 = Farmacia("Farmacia Bolivia", 1, "Ceja - calle 2")
f1.agregar(Medicamento("Aspirina", 201, "Dolor", 1.5))
f1.agregar(Medicamento("Antigripal", 212, "Resfrío", 5.0))
f1.agregar(Medicamento("Jarabe Dexametasona", 303, "Tos", 34.8))
archivo.agregar(f1)

f2 = Farmacia("Farmacorp", 2, "Av. 16 de julio")
f2.agregar(Medicamento("Golpex", 321, "Antinflamatorio Muscular", 13.5))
f2.agregar(Medicamento("Paracetamol", 102, "Dolor", 0.5))
archivo.agregar(f2)

archivo.guardar()
print("Guardado correctamente.\n")

print("=== Archivo completo ===")
archivo.mostrar_todo()

print("=== Medicamentos para tos en sucursal 1 ===")
archivo.mostrar_medicamentos_para_tos_sucursal(1)

print('\n=== Sucursales con medicamento "Golpex" ===')
archivo.mostrar_sucursales_con_medicamento("Golpex")
