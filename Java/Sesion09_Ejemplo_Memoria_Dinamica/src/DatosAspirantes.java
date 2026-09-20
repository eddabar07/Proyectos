/**
 * Consideraciones para el desarrollo de la app:
 * Se debe almacear los siguientes datos del aspirante: nombre completo,
 * edad, direccion, telefono, redes sociales, carreras interes,
 * escuela de procedencia y bachillerato
 */

import java.util.Scanner;

public class DatosAspirantes {
    // Crear objeto de tipo Aspirante
    Aspirantes a = new Aspirantes();
    
    // Declaracion de variables
    Scanner sc = new Scanner(System.in);
    private String tel;
    private String buscar;
    private String escuelaProced;
    private String bachill;
    private int cantidad;
    private int edadAspirante;
    private String nombre [];
    private Object dire[];
    private String redes [][];
    String carreras [];
    

    // Solicitar el nombre del aspirante
    public Aspirantes nombreAspirante(){
        // Asiganr tamaño a nombre
        nombre = new String[3];

        // Solicitar datos al aspirante
        System.out.print("Apellido paterno: ");
        nombre [0] = sc.nextLine();

        System.out.print("Apellido materno: ");
        nombre [1] = sc.nextLine();

        System.out.print("Nombre(s): ");
        nombre [2] = sc.nextLine();
        
        // Asignar el nombre al objeto Aspirante
        a.setNombreCompleto(nombre);
        return a;
    }

    // Solicitar edad del aspirante
    public Aspirantes edadAspirante(){
        // Solicitar la edad del aspirante
        System.out.print("Edad: ");
        edadAspirante = sc.nextInt();
        sc.nextLine();

        // Asignar la edad al objeto Aspirante
        a.setEdad(edadAspirante);
        return a;
    }

    // Solicitar direccion
    public Aspirantes direccionAspirante(){
        // Asignar tamaño a dire
        dire = new Object[5];

        // Solicitar la direccion del aspirante
        System.out.print("Calle: ");
        dire[0] = sc.nextLine();

        System.out.print("Número: ");
        dire[1] = sc.nextInt();
        sc.nextLine();

        System.out.print("Colonia: ");
        dire[2] = sc.nextLine();

        System.out.print("Código postal: ");
        dire[3] = sc.nextInt();
        sc.nextLine();

        System.out.print("Ciudad: ");
        dire[4] = sc.nextLine();

        // Asignar la direccion al objeto aspirante
        a.setDireccion(dire);
        return a;
    }

    // Solicitar el numero de telefono
    public Aspirantes telefonoAspirante(){
        // Solicitar el numero de telefono
        System.out.print("Número de teléfono: ");
        tel = sc.nextLine();

        // Asignar el numero de telefono al objeto Aspirante
        a.setTelefono(tel);
        return a;
    }

    // Solicitar redes sociales
    public Aspirantes redesSocialesAspirante(){
        // Solicitar la cantidad de redes a ingresar
        System.out.print("¿Cuántas redes sociales deseas ingresar?: ");
        cantidad = sc.nextInt();
        sc.nextLine();

        // Asignar tamaño a redes
        redes = new String[cantidad][2];

        // Ingresar redes sociales y nombre de usuario
        for (int i = 0; i < cantidad; i++){
            System.out.print("Nombre de la red social: ");
            redes [i][0] = sc.nextLine();

            System.out.print("Nombre de usuario: ");
            redes [i][1] = sc.nextLine();
        }

        // Asignar redes sociales al objeto Aspirante
        a.setRedesSociales(redes);
        return a;
    }

    // Solicitar la carrera de interes
    public Aspirantes carreraInteres(){
        // Asignar valores a carreras
        carreras = new String[]{
            "ingenieria en sistemas computacionales",
            "ingenieria mecatronica", 
            "ingenieria en industrias alimentarias",
            "licenciatura en administracion",
            "licenciatura en contador publico"
        };

        //Solicitar carrera de interes hasta que sea valida
        while (true){
            System.out.print("Carrera de interes: ");
            buscar = sc.nextLine().toLowerCase().trim();

            // Recorrer el arreglo de carreras
            for (int i = 0; i < carreras.length; i++){
                // Validar si la carrera esta disponible
                if (carreras[i].toLowerCase().equals(buscar)){
                    System.out.println("La carrera " + carreras[i] + " esta disponible");

                    // Asignar carrera al objeto Aspirante
                    a.setCarreraInteres(carreras[i]);
                    return a;
                }
            }
            System.out.println("La carrera no esta disponible. Intenta nuevamente.");
        }
    }

    // Solicitar escuela de procedencia
    public Aspirantes escuelaProcedencia(){
        // Solicitar escuela de procedencia
        System.out.print("Escuela de procedencia: ");
        escuelaProced = sc.nextLine();

        // Asignar escuela de procedencia al objeto Aspirante
        a.setEscuelaProcedencia(escuelaProced);
        return a;
    }

    // Solicitar bachillerato
    public Aspirantes bachillerato(){
        // Solicitar bachillerarto
        System.out.print("Bachillerato cursado: ");
        bachill = sc.nextLine();

        // Asiganar bachilleraro al objeto Aspirante
        a.setBachillerato(bachill);
        return a;
    }

    // Obtener datos de Aspirante
    public Aspirantes obtener(){
        nombreAspirante();
        edadAspirante();
        System.out.println();
        direccionAspirante();
        System.out.println();
        telefonoAspirante();
        System.out.println();
        redesSocialesAspirante();
        System.out.println();
        carreraInteres();
        System.out.println();
        escuelaProcedencia();
        bachillerato();

        return a;
    }
}