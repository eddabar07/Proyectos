import java.util.ArrayList;

/**
 * Clases WRAPPER (Envoltorio)
 * 
 * Crean o convierten datos primitivos en Objetos
 * 
 * Enteros
 *  byte -> Byte
 *  short -> Short
 *  int -> Integer
 *  long -> Long
 * 
 * Reales
 *  float -> Float
 *  double -> Double
 * 
 * Boolean
 *  boolean -> Boolean
 * 
 * Caracter
 *  char -> Character
 */

public class PruebaGenericos {
    public static void main(String[] args) {
        System.out.println("---------- Clases WRAPPER ----------");

        double temp = 45.26;
        Double temp2 = 23.4;

        System.out.println(temp * 100);
        System.out.println(temp2 * 100);

        String temp3 = "89.7";
        System.out.println(Double.parseDouble(temp3) * 100);

        int edad = 45;
        Integer edad2 = 25;

        System.out.println(edad * 100);
        System.out.println(edad2 * 100);

        int n1 = 0234;
        int n2 = 0x12345A;

        System.out.println(n1);
        System.out.println(n2);

        System.out.println(Integer.toBinaryString(1000));
        System.out.println(Integer.toHexString(1000));
        System.out.println(Integer.toOctalString(1000));

        System.out.println("---------- Genericos ----------");

        byte edades[] = {45, 23, 15, 60, 50};
        System.out.println(edades);

        // Mostrar las edades ordenadas de manera Ascendente
        ArrayList <Integer> listaEdades = new ArrayList<Integer>();

        listaEdades.add(45);
        listaEdades.add(23);
        listaEdades.add(15);
        listaEdades.add(60);
        listaEdades.add(50);

        System.out.println(listaEdades);

        listaEdades.sort(null);
        System.out.println(listaEdades);

        listaEdades.reversed();
        System.out.println(listaEdades);
    }
}
