package persistencia;

import java.util.ArrayList;

public class ArchivoCliente {
    public ArrayList<Cliente> clientes;

    public ArchivoCliente() {
        clientes = new ArrayList<>();
    }

    public void guardarCliente(Cliente c) {
        for (Cliente cliente : clientes) {
            if (cliente.id == c.id) {
                System.out.println("Cliente con ID " + c.id + " ya existe. No se agregó.");
                return;
            }
        }
        clientes.add(c);
    }

    public Cliente buscarCliente(String nombre) {
        for (Cliente c : clientes) {
            if (c.nombre.equalsIgnoreCase(nombre)) {
                return c;
            }
        }
        return null;
    }

    public Cliente buscarCliente(int id) {
        for (Cliente c : clientes) {
            if (c.id == id) {
                return c;
            }
        }
        return null;
    }

    public void buscarCelularCliente(int id) {
        Cliente c = buscarCliente(id);
        if (c != null) {
            System.out.println("ID: " + c.id + ", Nombre: " + c.nombre + ", Edad: " + c.edad + ", Ciudad: " + c.ciudad + ", Celular: " + c.celular);
        } else {
            System.out.println("Cliente con ID " + id + " no encontrado.");
        }
    }

    public void mostrarClientesCiudad(String ciudad) {
        boolean encontrado = false;
        for (Cliente c : clientes) {
            if (c.ciudad.equalsIgnoreCase(ciudad)) {
                System.out.println(c.nombre + ", " + c.edad + ", " + c.ciudad + ", " + c.celular);
                encontrado = true;
            }
        }
        if (!encontrado) {
            System.out.println("No hay clientes en la ciudad: " + ciudad);
        }
    }
}
