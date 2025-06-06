import json
import os

class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "salario": self.salario
        }

    @staticmethod
    def from_dict(data):
        return Empleado(data["nombre"], data["edad"], data["salario"])

class ArchivoEmpleado:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.empleados = self.cargar_empleados()

    def cargar_empleados(self):
        if not os.path.exists(self.nombre_archivo):
            return []
        with open(self.nombre_archivo, 'r') as f:
            try:
                data = json.load(f)
                return [Empleado.from_dict(e) for e in data]
            except json.JSONDecodeError:
                return []

    def guardar_empleados(self):
        with open(self.nombre_archivo, 'w') as f:
            json.dump([e.to_dict() for e in self.empleados], f, indent=4)

    def guardar_empleado(self, e):
        self.empleados.append(e)
        self.guardar_empleados()

    def busca_empleado(self, nombre):
        for e in self.empleados:
            if e.nombre == nombre:
                return e
        return None

    def mayor_salario(self):
        if not self.empleados:
            return None
        return max(self.empleados, key=lambda e: e.salario)

archivo = ArchivoEmpleado("empleados.json")

archivo.guardar_empleado(Empleado("Jose", 27, 1800))
archivo.guardar_empleado(Empleado("Carla", 38, 2150))
archivo.guardar_empleado(Empleado("Cristian", 33, 4800))

buscado = archivo.busca_empleado("Jose")
if buscado:
    print(f"Encontrado: {buscado.nombre}, {buscado.salario}")
else:
    print("Empleado no encontrado.")

mayor = archivo.mayor_salario()
if mayor:
    print(f"Mayor salario: {mayor.nombre}, {mayor.salario}")
else:
    print("No hay empleados.")
