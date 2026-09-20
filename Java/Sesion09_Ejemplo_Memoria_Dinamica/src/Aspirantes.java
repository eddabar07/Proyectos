public class Aspirantes {
    // Declaracion de variables de instancia
    private String [] nombreCompleto;
    private int edad;
    private int tamaño;
    private Object [] direccion;
    private String telefono;
    private String [][] redesSociales;
    private String carreraInteres;
    private String escuelaProcedencia;
    private String bachillerato;

    // Metodo Constructor
    public Aspirantes(String[] nombreCompleto, int edad, int tamaño, Object[] direccion, String telefono, String[][] redesSociales,
            String carreraInteres, String escuelaProcedencia, String bachillerato) {
        this.nombreCompleto = nombreCompleto;
        this.edad = edad;
        this.tamaño = tamaño;
        this.direccion = direccion;
        this.telefono = telefono;
        this.redesSociales = redesSociales;
        this.carreraInteres = carreraInteres;
        this.escuelaProcedencia = escuelaProcedencia;
        this.bachillerato = bachillerato;
    }

    public Aspirantes(){}

    // Getters and Setters
    public String[] getNombreCompleto() {
        return nombreCompleto;
    }

    public void setNombreCompleto(String[] nombreCompleto) {
        this.nombreCompleto = nombreCompleto;
    }

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public int getTamaño(){
        return tamaño;
    }

    public void setTamaño(int tamaño){
        this.tamaño = tamaño;
    }

    public Object[] getDireccion() {
        return direccion;
    }

    public void setDireccion(Object[] direccion) {
        this.direccion = direccion;
    }

    public String getTelefono() {
        return telefono;
    }

    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }

    public String[][] getRedesSociales() {
        return redesSociales;
    }

    public void setRedesSociales(String[][] redesSociales) {
        this.redesSociales = redesSociales;
    }

    public String getCarreraInteres() {
        return carreraInteres;
    }

    public void setCarreraInteres(String carreraInteres) {
        this.carreraInteres = carreraInteres;
    }

    public String getEscuelaProcedencia() {
        return escuelaProcedencia;
    }

    public void setEscuelaProcedencia(String escuelaProcedencia) {
        this.escuelaProcedencia = escuelaProcedencia;
    }

    public String getBachillerato() {
        return bachillerato;
    }

    public void setBachillerato(String bachillerato) {
        this.bachillerato = bachillerato;
    }

    @Override
    public String toString() {
        String texto = "";

        texto += "Nombre: " + nombreCompleto[0] + " " + nombreCompleto[1] + " "
        + nombreCompleto[2];

        texto += "\nEdad: " + edad;

        texto += "\n";

        texto += "\nDireccion: \n" + 
        "Calle: " + direccion[0] + 
        "\nNúmero: " + direccion[1] + 
        "\nColonia: " + direccion[2] +
        "\nCódigo Postal: " + direccion[3] + 
        "\nCiudad: " + direccion[4];

        texto += "\n";

        texto += "\nTelefono: " + telefono;

        texto += "\n";

        texto += "\nRedes sociales:";
        if (redesSociales != null && redesSociales.length > 0){
            for (int i = 0; i < redesSociales.length; i++) {
                texto += "\n" + redesSociales[i][0] + ": " + redesSociales[i][1];
            }
        }
        else{
            texto += "Ninguna";
        }

        texto += "\n";

        texto += "\nCarrera de interes: " + carreraInteres;

        texto += "\n";

        texto += "\nEscuela de procedencia: " + escuelaProcedencia;
        texto += "\nBachillerato: " + bachillerato;

        return texto;
    }
}