import java.util.ArrayList;
import java.util.Scanner;

public class RegistroAspirante {
    // Instanciar objeto de clase Datos Aspirantes
    DatosAspirantes da = new DatosAspirantes();
    Scanner sc = new Scanner(System.in);

    // Crear una lista de tipo Aspirante
    ArrayList <Aspirantes> listaAspirante = new ArrayList<>();

    // Añadir aspirante a la lista
    public void añadirAspirante(){
        listaAspirante.add(da.obtener());
    }

    // Eliminar aspirante 
    public void eliminarAspirante(){
        // Validar si la lista no esta vacia
        if (listaAspirante.isEmpty()){
            System.out.println("No hay aspirantes registrados");
            return;
        }

        // Solicitar nombre del aspirante
            System.out.print("Nombre del Aspirante: ");
            String name = sc.nextLine();
            System.out.println();

        // Recorrer lista
        for (int i = 0; i < listaAspirante.size(); i++) {
            // Validar si existe y eliminarlo
            if (listaAspirante.get(i).getNombreCompleto()[2].equalsIgnoreCase(name)) {
                listaAspirante.remove(i);
                System.out.println("Aspirante eliminado.");
                return;
            }
        }
        System.out.println("Aspirante no encontrado.");
    }

    // Buscar aspirante
    public void buscarAspirante(){
        // Validar si la lista no esta vacia
        if (listaAspirante.isEmpty()){
            System.out.println("No hay aspirantes registrados");
            return;
        }

        // Solicitar nombre del aspirante
            System.out.print("Nombre del Aspirante: ");
            String name = sc.nextLine();
            System.out.println();

        // Recorrer lista
        for (int i = 0; i < listaAspirante.size(); i++) {
            // Validar si existe y mostrar el aspirante
            if (listaAspirante.get(i).getNombreCompleto()[2].equalsIgnoreCase(name)) {
                System.out.println("Aspirante encontrado:");
                System.out.println(listaAspirante.get(i));
                return;
            }
        }
        System.out.println("Aspirante no encontrado.");
    }

    // Mostrar listado de aspirantes
    public void mostrarLista(){
        if (listaAspirante.isEmpty()) {
            System.out.println("No hay aspirantes registrados");
            return;
        } 
        
        System.out.println("========== Listado de Aspirantes ==========");
        for (int i = 0; i < listaAspirante.size(); i++) {
            System.out.println("\nAspirante " + String.format("%03d", i + 1) + "\n");
            System.out.println(listaAspirante.get(i));
        }
    }
}