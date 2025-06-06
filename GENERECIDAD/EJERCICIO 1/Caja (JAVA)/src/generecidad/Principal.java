package generecidad;

class Caja<T> {
	private T contenido;
	public void guardar(T dato) {
		contenido = dato;
	}
	public T obtener() {
	    return contenido;
	}
}

public class Principal {
	public static void main(String[] args) {
	    Caja<String> cajaDeTexto = new Caja<String>();
	    cajaDeTexto.guardar("Herramientas");
	
	    Caja<Integer> cajaDeEntero = new Caja<Integer>();
	    cajaDeEntero.guardar(25);
	
	    System.out.println("Contenido de la caja 1: " + cajaDeTexto.obtener());
	    System.out.println("Cantidad de objetos que lleva la caja 2: " + cajaDeEntero.obtener());
	}
}
