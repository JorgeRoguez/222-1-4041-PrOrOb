class Celular:

    color = "black"
    capacity = "128 gigas"
    company = "telcel"
    
    def make_call(self,contacto):
        print("Llamando a "+contacto)
    
    def finish_call(self):
        print("Llamada terminada")
    
    def save_contact(self):
        print("Contacto guardado")

jorge_cel = Celular()
print(jorge_cel.color)
print(jorge_cel.company)
jorge_cel.make_call("Ceizel")
jorge_cel.finish_call()
jorge_cel.save_contact()

ceizel_cel = Celular()
print(ceizel_cel.company)
print(ceizel_cel.capacity)
ceizel_cel.make_call("Jorge")
ceizel_cel.finish_call()
ceizel_cel.save_contact()

