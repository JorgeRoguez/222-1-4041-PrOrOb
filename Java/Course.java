
public class Course {
    
    public String clave_clase;
    public String nombre_clase;
    public String nombre_maestro;
    public String salon;
    public String dia_clase;
    public String hora_clase;

    public Course(String clave_clase, String nombre_clase, String nombre_maestro, String salon, String dia_clase, String hora_clase){
        this.clave_clase = clave_clase;
        this.nombre_clase = nombre_clase;
        this.nombre_maestro = nombre_maestro;
        this.salon = salon;
        this.dia_clase = dia_clase;
        this.hora_clase = hora_clase;
    }

    public String bienvenida(){
        return "Bienvenido a la clase ";
    }

    public String instrucciones(){
        return "Favor de tomar asiento, apagar celular y guardar silencio. ";
    }

    public void despedida(){
        System.out.println("Agradecemos tu asistencia, ¡vuelve pronto!");
    }

    public String cambio_salon(String nuevo_salon, String nuevo_dia){
        return "Esta semana tu clase será en el salon "+nuevo_salon+" el dia "+nuevo_dia;
    }

    public String cambio_maestro(String nuevo_maestro, String nueva_hora){
        return "Tu maestro habitual se reportó enfermo, será sustituido por "+nuevo_maestro+" en el mismo salón a las "+nueva_hora+" horas";
    }

    public String cambio_materia(String nuevo_nombre_materia, String nueva_clave){
        return "El próximo ciclo, esta materia ambiará de nombre, quedando con el nombre "+nuevo_nombre_materia+" con clave "+nueva_clave;
    }
    
}

