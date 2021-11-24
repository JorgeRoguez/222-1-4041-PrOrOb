class computer:

    def __init__(self, id, cpu, keyboard, mouse):
        self.id = id
        self.cpu = cpu
        self.keyboard = keyboard
        self.mouse = mouse

    class cpu:
        def __init__(self, id_cpu, marca_cpu, modelo_cpu, memoria_cpu):
            self.id_cpu = id_cpu
            

    class keyboard:
        def __init__(self, id_keyboard, marca_keyboard, modelo_keyboard):
            self.id_keyboard = id_keyboard
            self.marca_keyboard = marca_keyboard
            self.modelo_keyboard = modelo_keyboard
    
    class mouse:
        def __init__(self, id_mouse, marca_mouse, modelo_mouse, tipo_mouse):
            self.id_mouse = id_mouse
            self.marca_mouse = marca_mouse
    
nuevo_teclado = computer.keyboard("T123", "Perfect Choice", "Tcl456")
print (nuevo_teclado.id_keyboard)