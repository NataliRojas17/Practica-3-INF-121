package persistencia;

public class Main {
    public static void main(String[] args) {
        ArchivoCliente archivo = new ArchivoCliente();

        archivo.guardarCliente(new Cliente(1, "Natali", 25, "La Paz", 76543210));
        archivo.guardarCliente(new Cliente(2, "Fernando", 30, "Santa Cruz", 71234567));
        archivo.guardarCliente(new Cliente(3, "Eduardo", 40, "La Paz", 79876543));

        Cliente buscado = archivo.buscarCliente("Natali");
        if (buscado != null)
            System.out.println("Encontrado: " + buscado.nombre + ", " + buscado.ciudad);
        else
            System.out.println("Cliente no encontrado.");

        System.out.println("\nClientes en La Paz:");
        archivo.mostrarClientesCiudad("La Paz");

        System.out.println("\nBuscar cliente por ID 2:");
        Cliente clientePorId = archivo.buscarCliente(2);
        if (clientePorId != null) {
            System.out.println("Cliente ID 2: " + clientePorId.nombre + ", " + clientePorId.ciudad);
        } else {
            System.out.println("Cliente no encontrado por ID.");
        }

        System.out.println("\nBuscar cliente y celular por ID 3:");
        archivo.buscarCelularCliente(3);
    }
}
