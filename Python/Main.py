class Computer:

    def __init__(self, id, cpu, keyboard, mouse, os):
        self.id = id
        self.cpu = cpu
        self.keyboard = keyboard
        self.mouse = mouse
        self.os = os
    
    def get_id(self):
        return self.id
    def get_cpu(self):
        return self.cpu
    def get_keyboard(self):
        return self.keyboard
    def get_mouse(self):
        return self.mouse
    def get_os(self):
        return self.os
    
    def show_computer(self):
        print("\nId: "+self.get_id()+"\nCpu: "+self.get_cpu()+"\nKeyboard: "+self.get_keyboard()+"\nMouse: "+self.get_mouse()+"\nOS "+self.get_os())

id = input("Favor de ingresar id: ")
cpu = input("Favor de ingresar cpu: ")
keyboard = input("Favor de ingresar keyboard: ")
mouse = input("Favor de ingresar mouse: ")
os = input("Favor de ingresar os: ")
new_computer = Computer(id, cpu, keyboard, mouse, os)
new_computer.show_computer()
