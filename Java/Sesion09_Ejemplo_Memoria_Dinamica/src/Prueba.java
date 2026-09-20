import java.util.Scanner;

public class Prueba {
    public static void main(String[] args) {
        // Crear objeto de registroAspirante
        RegistroAspirante registro = new RegistroAspirante();

        // Declaracion de variables
        Scanner sc = new Scanner(System.in);
        int opcion;

        // Menu de opciones
        do{
            System.out.println("\n========== Menú Aspirantes ==========");
            System.out.println("""
            1.- Ingresar Aspirante
            2.- Buscar Aspirante
            3.- Mostrar listado de Aspirantes
            4.- Eliminar Aspirante
            0.- Salir
            """);
            System.out.print("Ingresa una opción: ");
            opcion = sc.nextInt();
            sc.nextLine();
            System.out.println();

            switch (opcion) {
                case 1:
                    registro.añadirAspirante();
                    System.out.println("Aspirante Registrado Correctamente");
                    break;
                
                case 2:
                    registro.buscarAspirante();
                    break;

                case 3:
                    registro.mostrarLista();
                    break;
                
                case 4:
                    registro.eliminarAspirante();
                    System.out.println();
                    break;
                
                default:
                    System.out.println("Opción Incorrecta");
            }
        } while (opcion != 0);
        sc.close();
    }
}
