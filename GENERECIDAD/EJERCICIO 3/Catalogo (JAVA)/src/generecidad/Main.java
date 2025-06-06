package generecidad;

public class Main {
    public static void main(String[] args) {
 
        Catalogo<Libro> catalogoLibros = new Catalogo<>();
        catalogoLibros.agregarElemento(new Libro("Bajo la misma estrella ", "John Green"));
        catalogoLibros.agregarElemento(new Libro("Maravilloso desastre", "Jamie McGuire"));

        System.out.println("Catálogo de Libros:");
        catalogoLibros.mostrarElementos();
    }
}
