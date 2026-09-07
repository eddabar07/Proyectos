/*
Vectores en JAVA

    int datos [];
    datos = new [10];
    datos [4] = 100;

    int datos [] = new int[10];
    int datos [] = {90, 80, 100};

    Crear nuesra propia implementacion de VECTOR MUTABLE

    1) Datos -> vector de eneteros
    2) Crear 
    3) Llenar
    4) Agregar elemento al FINAL
    5) Agregar elemento al INICIO
    6) Mostrar elementos
    7) Eliminar elemento del INICIO
    8) Eliminar elemento del FINAL
*/

import java.util.Arrays;
import java.util.Scanner;

class TDAVectorEspecial{

    // Punto 1
    private byte datos [];

    // Punto 2
    public TDAVectorEspecial(int tam){
        datos = new byte[tam];   
    }

    // Punto 3
    public void llenarDatos() {
        Scanner sc = new Scanner(System.in);
        
        for(int i = 0; i < datos.length; i++){
            System.out.print("Ingresa el Valor " + (i+1) + ": ");
            datos[i] = sc.nextByte();
            
        }
        sc.close();
    }

    // Punto 6
    public void mostrarElementos() {
        System.out.print(Arrays.toString(datos));
    }
}


public class PruebaVectorEspecial {
    public static void main(String[] args) {
        
        int calif [] = new int [10];
        String nombres [] = new String [5];
        char c [] = new char [20];

        System.out.println(Arrays.toString(calif));
        System.out.println(Arrays.toString(nombres));
        System.out.println(Arrays.toString(c));

        TDAVectorEspecial tdaVectorEspecial = new TDAVectorEspecial(3);
        tdaVectorEspecial.llenarDatos();
        tdaVectorEspecial.mostrarElementos();

    }
}
