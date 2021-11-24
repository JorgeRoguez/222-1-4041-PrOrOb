class Person:

    def __init__(self, first_name, last_name):

        self.first_name = first_name
        self.last_name = last_name

    def say_hello_user(self,user_name):
        return "Hello "+user_name
    
    def matter(self, matter_name, matter_day):
        return "Materia: "+matter_name+" los dias "+matter_day
        
obj_person = Person("Jorge", "Roguez")
print(obj_person.first_name+" "+obj_person.last_name)
print(obj_person.say_hello_user("Bruno"))
print(obj_person.matter("PoOrOb", "martes"))

class Student(Person):

    def __init__(self, first_name, last_name, nick_name):
        Person.__init__(self, first_name, last_name)
        #super().__init__(first_name, last_name)
        self.nick_name = nick_name
    
    def student_id(self, student_id):
        return "Matricula: "+student_id
            
obj_student = Student("Ceizel", "Lopez", "la leona")
print(obj_student.first_name+" "+obj_student.last_name)
print(obj_student.nick_name)
print(obj_student.say_hello_user("Diego"))
print(obj_student.student_id("0120820333"))
print(obj_student.matter("Po Or Ob", "miercoles"))

class Basic_Student(Student):

    def __init__(self, first_name, last_name, nick_name, age):
        super().__init__(first_name, last_name, nick_name)
        self.age = age
    
    def student_file(self, gender, nationality):
        return "Genero: "+gender+" y de nacionalidad: "+nationality
    
    

obj_basic = Basic_Student("Bruno", "Roguez", "el zurdo", "20")
print(obj_basic.first_name+" "+obj_basic.last_name+", "+obj_basic.nick_name+" de "+obj_basic.age+" años")
print(obj_basic.student_file("masculino", "mexicana"))