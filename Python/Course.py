class Course: 

    def __init__(self, clave_clase, nombre_clase, nombre_maestro, salon, dia_clase, hora_clase):
        self.clave_clase = clave_clase
        self.nombre_clase = nombre_clase
        self.nombre_maestro = nombre_maestro
        self.salon = salon
        self.dia_clase = dia_clase
        self.hora_clase = hora_clase

    def bienvenida(self):
        return "Bienvenido a la clase: "
    
    def instrucciones(self):
        return "Favor de tomar asiento, apagar celular y guardar silencio. "

    def despedida(self):
        return "Agradecemos tu asistencia, ¡vuelve pronto! "

    def cambio_salon(self, nuevo_salon, nuevo_dia):
        return "Esta semana tu clase será en el salon "+nuevo_salon+" el dia "+nuevo_dia

    def cambio_maestro(self, nuevo_maestro, nueva_hora):
        return "Tu maestro habitual se reportó enfermo, será sustituido por "+nuevo_maestro+" en el mismo salon a las "+nueva_hora+" horas"
    
    def cambio_materia(self, nuevo_nombre_materia, nueva_clave):
        return "El proximo ciclo, esta materia cambiara de nombre, quedando con el nombre "+nuevo_nombre_materia+" con clave "+nueva_clave


nueva_materia = Course("40142", "Pr Or Ob", "Luis Guerra", "5202", "Martes", "19:00 - 20:30")
print(nueva_materia.bienvenida())
print(nueva_materia.instrucciones())
print("")

print(nueva_materia.cambio_salon("5201", "Jueves"))
print(nueva_materia.cambio_maestro("Juan Perez", "19:15"))
print(nueva_materia.cambio_materia("POO", "5201"))
print("")

print(nueva_materia.despedida())
