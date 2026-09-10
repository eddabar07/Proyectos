package T1_A2_Vector_TDA;
/* 
Crear nuesra propia implementacion de VECTOR MUTABLE

1 -> Crear y llenar el arreglo
2 -> Obtener posición inicial
3 -> Obtener posición final
4 -> Obtener cantidad de elementos 
5 -> Mostrar todos los elementos
6 -> Mostrar elemento del inicio
7 -> Mostrar elemento del final
8 -> Aumentar tamaño del arreglo
9 -> Disminuir tamaño del arreglo 
10 -> Insertar elemento en posición especifica
11 -> Insertar elemento en al inicio
12 -> Insertar elemento al final
13 -> Eliminar elemento de posición especifica
14 -> Eliminar elemento del inicio
15 -> Eliminar elemento del final
16 -> Invertir el vector
17 -> Buscar elemento
0 -> Salir del Programa
*/

import java.util.Arrays;
import java.util.Scanner;

class VectorEspecial{
    Scanner sc = new Scanner(System.in);
    int datos [];
    int tamaño;

    // Constructor
    public VectorEspecial(){}

    // 1.- Crear
    public void crear(int capacidad){
        datos = new int[capacidad];
    }

    // 2.- Llenar
    public void llenar(int capacidad) {
        for (int i = 0; i < capacidad; i++) {
            System.out.print("Ingresa el elemento " + (i + 1) + ": ");
            datos[i] = sc.nextInt();
            tamaño++;
        }
    }

    // 3.- Obtener la posicion del INICIO
    public void obtenerPosicionInicio(){
        System.out.println("La posicion inicial es 0");
    }

    // 4.- Obtener posicion final
    public void obtenerPosicionFinal(){
        if (tamaño == 0) {
            System.out.println("El vector esta vacio.");
            return;
        }
        int indiceFinal = tamaño - 1;
        System.out.println("El indice final es: " + indiceFinal);
    }

    // 5.- Obtener la cantidad de elementos
    public void obtenerCantidadElementos(){
        System.out.println("El vector tiene: " + tamaño + " elementos");
    }

    // 6.- Mostrar el elemento del inicio
    public void mostrarElementoInicial(){
        if (tamaño == 0) {
            System.out.println("El vector esta vacio.");
            return;
        }
        int elementoInicial = datos[0];
        System.out.println("El elemento inicial es: " + elementoInicial);
    }

    // 7.- Mostrar el elemento del final
    public void MostrarElementoFinal(){
        if (tamaño == 0) {
            System.out.println("El vector esta vacio.");
            return;
        }
        int elementoFinal = datos[tamaño - 1];
        System.out.println("El elemento final es: " + elementoFinal);
    }

    // 8.- Aumentar el tamaño del arreglo
    public void aumentarTamaño(int incremento){
        int nuevaCapacidad = datos.length + incremento;
        int aumento [] = new int[nuevaCapacidad];
        System.arraycopy(datos, 0, aumento, 0, datos.length);
        datos = aumento;
        
        System.out.println("El nuevo tamaño del arreglo es de:" + datos.length + " indices");
    }

    // 9.- Disminuir el tamaño del arreglo
    public void disminuirTamaño(int decremento){
        int nuevaCapacidad = datos.length - decremento;
        int disminucion [] = Arrays.copyOfRange(datos, 0, nuevaCapacidad);

        if (nuevaCapacidad < 0) {
            System.out.println("No se puede disminuir esa cantidad.");
            return;
        }

        datos = disminucion;
        if (tamaño > datos.length) {
            tamaño = datos.length;
        }
        System.out.println("El nuevo tamaño del arreglo es de:" + datos.length + " indices");
    }

    // 10.- Insertar elemento en una posicion especifica
    public void instertarPosicionEspecifica(int nuevoElemento, int posicionInsertar){
        if (tamaño == datos.length){
            System.out.println("No se pueden agregar mas datos. El vector esta lleno");
            return;
        }
        if (posicionInsertar < 0 || posicionInsertar > tamaño) {
            System.out.println("Posicion invalida.");
            return;
        }

        for (int i = tamaño; i > posicionInsertar; i--) {
            datos[i] = datos[i - 1];
        }
        datos[posicionInsertar] = nuevoElemento;
        tamaño++;
    }

    // 11.- Insertar elemento al inicio
    public void agregarInicio(int valor) {
        if (tamaño == datos.length){
            System.out.println("No se pueden agregar mas datos. El vector esta lleno");
            return;
        }
        // Recorrer todo hacia la derecha para hacer espacio
        for (int i = tamaño; i > 0; i--) {
            datos[i] = datos[i - 1];
        }
        datos[0] = valor;
        tamaño++;
    }

    // 12.- Insertar elemento al final
    public void agregarFinal(int valor) {
        if (tamaño == datos.length){
            System.out.println("No se pueden agregar mas datos. El vector esta lleno");
            return;
        }
        datos[tamaño] = valor;
        tamaño++;
    }

    // 13.- Eliminar elemento en una posicion especifica
    public void eliminarPosicionEspecifica(int indiceEliminar){
        if (tamaño == 0) {
            System.out.println("El vector esta vacio.");
            return;
        }
        if (indiceEliminar < 0 || indiceEliminar >= tamaño) {
            System.out.println("Posicion invalida.");
            return;
        }

        for (int i = indiceEliminar; i < tamaño - 1; i++) {
            datos[i] = datos[i + 1];
        }
        datos[tamaño - 1] = 0;
        tamaño--;
    }

    // 14.- Eliminar elemento al inicio
    public void eliminarInicio() {
        if (tamaño == 0) {
            System.out.println("El vector esta vacio.");
            return;
        }
        // Recorrer todo hacia la izquierda
        for (int i = 0; i < tamaño - 1; i++) {
            datos[i] = datos[i + 1];
        }
        datos[tamaño - 1] = 0;
        tamaño--;
    }

    // 15.- Eliminar elemento al final
    public void eliminarFinal() {
        if (tamaño == 0) {
            System.out.println("El vector esta vacio.");
            return;
        }
        datos[tamaño - 1] = 0;
        tamaño--;
    }

    // 16.- Invertir vector
    public void invertirVector(){
        for (int i = 0; i < tamaño / 2; i++){
            int temporal = datos[i];
            int inverso  = tamaño - 1 - i;
            datos[i] = datos[inverso];
            datos[inverso] = temporal;
        }
    }

    // 17.- Buscar un elemento especifico
    public void buscarElemento(int elemento){
        int posicionEncontrada = -1;
        for (int i = 0; i < tamaño; i++){
            if (datos[i] == elemento){
                posicionEncontrada = i;
                break;
            }
        }

        if (posicionEncontrada == -1) {
            System.out.println("No se encontro el elemento " + elemento);
        } else {
            System.out.println("Elemento encontrado en la posicion: " + posicionEncontrada);
        }
    }

    // 18.- Mostrar elementos
    public void mostrar() {
        System.out.print("Vector: [");
        for (int i = 0; i < tamaño; i++) {
            System.out.print(datos[i]);
            if (i < tamaño - 1) {
                System.out.print(", ");
            }
        }
        System.out.println("]");
    }
}

public class Problema2VectorEspecial {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        VectorEspecial ve = new VectorEspecial();
        int opcion;

        do{
        System.out.print("\n");
        System.out.println("""
            1 -> Crear y llenar el arreglo
            2 -> Obtener posición inicial
            3 -> Obtener posición final
            4 -> Obtener cantidad de elementos
            5 -> Mostrar todos los elementos
            6 -> Mostrar elemento del inicio
            7 -> Mostrar elemento del final
            8 -> Aumentar tamaño del arreglo
            9 -> Disminuir tamaño del arreglo
            10 -> Insertar elemento en posición especifica
            11 -> Insertar elemento en al inicio
            12 -> Insertar elemento al final
            13 -> Eliminar elemento de posición especifica
            14 -> Eliminar elemento del inicio
            15 -> Eliminar elemento del final
            16 -> Invertir el vector
            17 -> Buscar elemento
            0 -> Salir del Programa
            """);
        System.out.print("Ingresa una opcion: ");
        opcion = sc.nextInt();
        
        switch (opcion) {
            case 1:
                System.out.print("Ingresa el tamaño del vector: "); 
                    ve.crear(sc.nextInt());
                    System.out.print("¿Cuantos elementos deseas ingresar?: ");
                    ve.llenar(sc.nextInt());
                break;
            case 2:
                ve.obtenerPosicionInicio();
                break;
            case 3:
                ve.obtenerPosicionFinal();
                break;
            case 4:
                ve.obtenerCantidadElementos();
                break;
            case 5:
                ve.mostrar();
                break;
            case 6:
                ve.mostrarElementoInicial();
                break;
            case 7:
                ve.MostrarElementoFinal();
                break;
            case 8:
                System.out.println("Ingresa cuantos indices deseas AGREGAR al arreglo: ");
                ve.aumentarTamaño(sc.nextInt());
                break;
            case 9:
                System.out.println("Ingresa cuantos indices deseas QUITARLE al arreglo: ");
                ve.disminuirTamaño(sc.nextInt());
                break;
            case 10:
                System.out.println("Ingresa el valor a insertar: ");
                int nuevoElemento = sc.nextInt();

                System.out.println("Ingresa la POSICION donde insertar: ");
                int posicionInsertar = sc.nextInt();

                ve.instertarPosicionEspecifica(nuevoElemento, posicionInsertar);
                break;
            case 11:
                System.out.println("Valor a agregar al INICIO: ");
                ve.agregarInicio(sc.nextInt());
                break;
            case 12:
                System.out.println("Valor a agregar al FINAL: ");
                ve.agregarFinal(sc.nextInt());
                break;
            case 13:
                System.out.println("Ingresa la POSICION del elemento a eliminar: ");
                ve.eliminarPosicionEspecifica(sc.nextInt());
                break;
            case 14:
                ve.eliminarInicio();
                break;
            case 15:
                ve.eliminarFinal();
                break;
            case 16:
                ve.invertirVector();
                break;
            case 17:
                System.out.println("Ingresa el elemento a BUSCAR: ");
                ve.buscarElemento(sc.nextInt());
                break;
            case 0: 
                System.out.println("Saliendo del programa...");
                System.exit(0);
                break;
            default:
                System.out.println("Opcion Incorrecta, Intente de Nuevo");
        }
    } while (opcion != 0);
    sc.close();

    }
}