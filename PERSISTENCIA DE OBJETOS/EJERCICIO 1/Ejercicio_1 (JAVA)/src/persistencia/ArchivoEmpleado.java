package persistencia;

import java.io.*;
import java.util.ArrayList;

public class ArchivoEmpleado {
    public ArrayList<Empleado> empleados;
    private final String nombreArchivo = "empleados.dat";

    public ArchivoEmpleado() {
        empleados = cargarEmpleados();
    }

    @SuppressWarnings("unchecked")
    private ArrayList<Empleado> cargarEmpleados() {
        File archivo = new File(nombreArchivo);
        if (!archivo.exists()) {
            return new ArrayList<>();
        }
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(archivo))) {
            return (ArrayList<Empleado>) ois.readObject();
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
            return new ArrayList<>();
        }
    }

    private void guardarEmpleados() {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(nombreArchivo))) {
            oos.writeObject(empleados);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void guardarEmpleado(Empleado e) {
        empleados.add(e);
        guardarEmpleados();
    }

    public Empleado buscaEmpleado(String nombre) {
        for (Empleado e : empleados)
            if (e.nombre.equalsIgnoreCase(nombre)) return e;
        return null;
    }

    public Empleado mayorSalario() {
        if (empleados.isEmpty()) return null;
        Empleado mayor = empleados.get(0);
        for (Empleado e : empleados) {
            if (e.salario > mayor.salario) {
                mayor = e;
            }
        }
        return mayor;
    }
}
