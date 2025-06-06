package persistencia;

public class Cliente {
    public int id;
    public String nombre;
    public int edad;
    public String ciudad;
    public int celular;

    public Cliente(int id, String nombre, int edad, String ciudad, int celular) {
        this.id = id;
        this.nombre = nombre;
        this.edad = edad;
        this.ciudad = ciudad;
        this.celular = celular;
    }
}
