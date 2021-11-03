public class Course {

    public String id_alumno;
    public String nombre_alumno;
    public String correo_electronico;
    public float calificacion;
    public String materia;
    public String nombre_maestro;

    public Course(String id_alumno,String nombre_alumno,String correo_electronico,float calificacion,String materia,String nombre_maestro){
        this.id_alumno = id_alumno;
        this.nombre_alumno = nombre_alumno;
        this.correo_electronico = correo_electronico;
        this.calificacion = calificacion;
        this.materia = materia;
        this.nombre_maestro = nombre_maestro;   
    }

    public static void presentacion(String[] args) {
        Course alumno1 = new this.id_alumno("0120820333");
        Course alumno1 = new this.nombre_alumno("Jorge Roguez");
        Course alumno1 = new this.correo_electronico("joroguez@gmail.com");
        Course alumno1 = new this.calificacion(8.5);
        Course alumno1 = new this.materia("PrOrOb");
        Course alumno1 = new this.nombre_maestro("Luis Guerra");

        System.out.println("Id: "+alumno1.id_alumno());
        System.out.println("Nombre: "+alumno1.nombre_alumno());
        System.out.println("Correo: "+alumno1.correo_electronico());
        System.out.println("Calificacion: "+alumno1.calificacion());
        System.out.println("Materia: "+alumno1.materia());
        System.out.println("Maestro: "+alumno1.nombre_maestro());
    }

   Course.presentacion()
}