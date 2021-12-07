class Computer:

    def __init__(self, id, cpu, keyboard, mouse, os):
        self.id = id
        self.cpu = cpu
        self.keyboard = keyboard
        self.mouse = mouse
        self.os = os
    
class Cpu(Computer):

    def __init__(self, cpu_id, cpu_brand, cpu_model):
        self.cpu_id = cpu_id
        self.cpu_brand = cpu_brand
        self.cpu_model = cpu_model
    
    def get_cpu_id(self):
        return self.cpu_id
    def get_cpu_brand(self):
        return self.cpu_brand
    def get_cpu_model(self):
        return self.cpu_model

    def show_cpu(self):
        print("\nLos datos del CPU son:\nId: "+self.get_cpu_id()+"\nMarca: "+self.get_cpu_brand()+"\nModelo: "+self.get_cpu_model())

class Keyboard(Computer):

    def __init__(self, keyboard_id, keyboard_brand, keyboard_model):
        self.keyboard_id = keyboard_id
        self.keyboard_brand = keyboard_brand
        self.keyboard_model = keyboard_model
    
    def get_keyboard_id(self):
        return self.keyboard_id
    def get_keyboard_brand(self):
        return self.keyboard_brand
    def get_keyboard_model(self):
        return self.keyboard_model
    
    def show_keyboard(self):
        print("\nLos datos del teclado son:\nId: "+self.get_keyboard_id()+"\nMarca: "+self.get_keyboard_brand()+"\nModelo: "+self.get_keyboard_model())

class Mouse(Computer):

    def __init__(self, mouse_id, mouse_brand, mouse_model, mouse_type):
        self.mouse_id = mouse_id
        self.mouse_brand = mouse_brand
        self.mouse_model = mouse_model
        self.mouse_type = mouse_type
    
    def get_mouse_id(self):
        return self.mouse_id
    def get_mouse_brand(self):
        return self.mouse_brand
    def get_mouse_model(self):
        return self.mouse_model
    def get_mouse_type(self):
        return self.mouse_type
    
    def show_mouse(self):
        print("\nLos datos del mouse son:\nId: "+self.get_mouse_id()+"\nMarca: "+self.get_mouse_brand()+"\nModelo: "+self.get_mouse_model()+"\nTipo: "+self.get_mouse_type())

class Os(Computer):

    def __init__(self, os_id, os_brand, os_model):
        self.os_id = os_id
        self.os_brand = os_brand
        self.os_model = os_model
    
    def get_os_id(self):
        return self.os_id
    def get_os_brand(self):
        return self.os_brand
    def get_os_model(self):
        return self.os_model
    
    def show_os(self):
        print("\nLos datos del OS son:\nId: "+self.get_os_id()+"\nMarca: "+self.get_os_brand()+"\nModelo: "+self.get_os_model())


cpu_id = input("\nIngresa el ID del CPU: ")
cpu_brand = input("Ingresa la marca del CPU: ")
cpu_model = input("Ingresa el modelo del CPU: ")

keyboard_id = input("\nIngresa el ID del teclado: ")
keyboard_brand = input("Ingresa la marca del teclado: ")
keyboard_model = input("Ingresa el modelo del teclado: ")

mouse_id = input("\nIngresa el ID del mouse: ")
mouse_brand = input("Ingresa la marca del mouse: ")
mouse_model = input("Ingresa el modelo del mouse: ")
mouse_type = input("Ingresa el tipo del mouse: ")

os_id = input("\nIngresa el ID del sistema operativo: ")
os_brand = input("Ingresa la marca del sistema operativo: ")
os_model = input("Ingresa el modelo del sistema operativo: ")

new_cpu = Cpu(cpu_id, cpu_brand, cpu_model)
new_keyboard = Keyboard(keyboard_id, keyboard_brand, keyboard_model)
new_mouse = Mouse(mouse_id, mouse_brand, mouse_model, mouse_type)
new_os = Os(os_id, os_brand, os_model)

new_cpu.show_cpu()
new_keyboard.show_keyboard()
new_mouse.show_mouse()
new_os.show_os()
