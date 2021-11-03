
class Course(): 

    def __init__(self, id_alumno, nombre_alumno, correo_electronico, calificacion, materia, nombre_maestro):
        self.id_alumno = id_alumno
        self.nombre_alumno = nombre_alumno
        self.correo_electronico = correo_electronico
        self.calificacion = calificacion
        self.materia = materia
        self.nombre_maestro = nombre_maestro
    
    def alumno(self):
        presentacion = ("Id: \t\t{}\nNombre: \t{}\nCorreo: \t{}\nCalificacion: \t{}\nMateria: \t{}\nMaestro: \t{}")
        print(presentacion.format(self.id_alumno, self.nombre_alumno, self.correo_electronico, self.calificacion, self.materia, self.nombre_maestro))

    def cambio_calif(self):
        temporal = input("\n¿Desea cambiar la calificacion? (s/n) ")
        if (temporal == "s"):
            self.calificacion = input("\n¿Cual es la calificacion nueva? ")
            Alumno1.alumno()
            print("Estos son los datos del alumno con la nueva calificacion.")

Alumno1 = Course("0120820333", "Jorge Roguez", "joroguez@gmail.com", 8.5, "PrOrOb", "Luis Guerra")
Alumno2 = Course("0123456789", "Juan Perez", "juanito@gmail.com", 8.5, "PrOrOb", "Luis Guerra")

Alumno1.alumno()
Alumno1.cambio_calif()
print("\n")
Alumno2.alumno()