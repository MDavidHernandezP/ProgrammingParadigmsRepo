#Unidad 2, programación orientada  objetos

#1. Class
class Humano:
    # 2. Instance
    def __init__(self, altura):
        self.alturita = altura
        self.edad = 25
        print(f"Mides {self.alturita} y tienes {self.edad} años")

    # 3. Object
    def hablar(self, mensaje):
        print(mensaje)

# 4. Message
pedro = Humano(178)
pedro.hablar("Hola, Mucho gusto")

""" Parte potente """

# 5. Inheritance!!!
class Cholo(Humano):
    def __init__(self, altura, nombrecholo, edad):
        super().__init__(altura)
        self.nombre = nombrecholo
        self.edad = edad
        self.navajas = []

    def navajazo(self):
        print("Bum! Te meto un navajazo.")

    # 7. Abstraction!!!
    def navaja(self, tipodenavaja):
        self.navajas.append(tipodenavaja)
        print(f"Ahora tienes una navaja: {tipodenavaja}")

# 6. Polymorphism!!!
def saludodecholo(algo):
    algo.navajazo()

cholito = Cholo(178, "Brayan", 15)
saludodecholo(cholito)

# 8. Encapsulation
cholito.navaja("Suiza")
cholito.navaja("Un machete")

# Accessing the encapsulated course list
print(f"{cholito.nombre} Tienes estas navajas {cholito.navajas}")