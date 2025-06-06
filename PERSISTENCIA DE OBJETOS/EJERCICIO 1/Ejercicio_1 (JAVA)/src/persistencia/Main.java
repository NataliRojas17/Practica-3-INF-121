package persistencia;

public class Main {
    public static void main(String[] args) {
        ArchivoEmpleado archivo = new ArchivoEmpleado();

        if (archivo.empleados.isEmpty()) {
            archivo.guardarEmpleado(new Empleado("Jose", 27, 1800));
            archivo.guardarEmpleado(new Empleado("Carla", 38, 2150));
            archivo.guardarEmpleado(new Empleado("Cristian", 33, 4800));
        }

        Empleado buscado = archivo.buscaEmpleado("Carla");
        if (buscado != null)
            System.out.println("Encontrado: " + buscado.nombre + ", " + buscado.salario);
        else
            System.out.println("Empleado no encontrado.");

        Empleado mayor = archivo.mayorSalario();
        if (mayor != null)
            System.out.println("Mayor salario: " + mayor.nombre + ", " + mayor.salario);
        else
            System.out.println("No hay empleados.");
    }
}
