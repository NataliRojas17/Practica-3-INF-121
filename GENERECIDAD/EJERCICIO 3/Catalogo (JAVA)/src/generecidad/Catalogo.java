package generecidad;

import java.util.ArrayList;

public class Catalogo<T> {
    private ArrayList<T> elementos;
    public Catalogo() {
        elementos = new ArrayList<>();
    }
    public void agregarElemento(T elemento) {
        elementos.add(elemento);
    }
    public T buscarElemento(int indice) {
        if (indice >= 0 && indice < elementos.size()) {
            return elementos.get(indice);
        } else {
            return null;
        }
    }
    public void mostrarElementos() {
        for (T elemento : elementos) {
            System.out.println(elemento);
        }
    }
}
