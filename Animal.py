class Animal:

    size = "pequeño"

    def eat(self):
        print("Comiendo...")

    def playing_ball(self, ball_color):
        print("Atrapando la bola "+ ball_color)

dog_one = Animal()
print(dog_one)
print("Tamaño "+ dog_one.size)
dog_one.eat()
dog_one.playing_ball("azul")
cat_one = Animal()
print(cat_one)
print("Tamaño "+ cat_one.size)
cat_one.playing_ball("roja")