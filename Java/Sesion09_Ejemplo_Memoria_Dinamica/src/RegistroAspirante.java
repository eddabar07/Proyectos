import java.util.ArrayList;
import java.util.Scanner;

public class RegistroAspirante {
    // Instanciar objeto de clase Datos Aspirantes
    Aspirantes a = new Aspirantes();
    DatosAspirantes da = new DatosAspirantes();
    Scanner sc = new Scanner(System.in);

    // Crear una lista de tipo Aspirante
    ArrayList <Aspirantes> listaAspirante = new ArrayList<>();

    // Generar folio Aspirante
    public Aspirantes folAspirantes(){
        int folioAsp = listaAspirante.size() + 1;

        a.setFolio(folioAsp);
        return a;
    }

    // Añadir aspirante a la lista
    public void añadirAspirante(){
        listaAspirante.add(da.obtener());
    }

    // Eliminar aspirante 
    public void eliminarAspiranteNombre(){
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

    public void eliminarAspiranteFolio(){
        // Validar si la lista no esta vacia
        if (listaAspirante.isEmpty()){
            System.out.println("No hay aspirantes registrados");
            return;
        }

        // Solicitar nombre del aspirante
            System.out.print("Folio del Aspirante: ");
            int folioAspi = sc.nextInt();
            System.out.println();

        // Recorrer lista
        for (int i = 0; i < listaAspirante.size(); i++) {
            // Validar si existe y eliminarlo
            if (listaAspirante.get(i).getFolio() == folioAspi) {
                listaAspirante.remove(i);
                System.out.println("Aspirante eliminado.");
                return;
            }
        }
        System.out.println("Aspirante no encontrado.");
    }

    // Buscar aspirante
    public void buscarAspiranteNombre(){
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

    public void buscarAspiranteFolio(){
        // Validar si la lista no esta vacia
        if (listaAspirante.isEmpty()){
            System.out.println("No hay aspirantes registrados");
            return;
        }

        // Solicitar nombre del aspirante
            System.out.print("Folio del Aspirante: ");
            int folio = sc.nextInt();
            System.out.println();

        // Recorrer lista
        for (int i = 0; i < listaAspirante.size(); i++) {
            // Validar si existe y mostrar el aspirante
            if (listaAspirante.get(i).getFolio() == folio) {
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
            System.out.println(listaAspirante.get(i));
        }
    }
}