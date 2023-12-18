#Vehicle Management at an Auto Workshop:
#An auto workshop needs a system to manage vehicle information. 
#To achieve this, they use:
#Encapsulation: Create a Vehicle class with private attributes, such as model and manufacturing year, and methods to access and modify these attributes.
#Inheritance: Derive classes like Car and Motorcycle from the base class Vehicle.
#Polymorphism:Implement methods like accelerate and brake in the subclasses to simulate the specific behavior of each type of vehicle.
#Abstraction:Utilize an abstract class Vehicle with abstract methods to represent common actions, such as start.

#Encapsulation
class Vehicle:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def acces(self):
        print(f"El modelo y año del carro son: {self.model} y {self.year} respectivamente. ")

    def modify(self, model, year):
        print(f"Cambiando el modelo y año del carro. ")
        self.model = model
        self.year = year
        print(f"El modelo y año del carro ahora son: {self.model} y {self.year} respectivamente. ")

#Inheritance
class Car(Vehicle):
    def __init__(self, model, year, carname, owner):
        super().__init__(model, year)
        self.name = carname
        self.owner = owner

    #Polymorphism
    def accelerate(self):
        print("El carro está acelerando con su pedal. ")

    def brake(self):
        print("El carro está frenando con su pedal de freno. ")

#Inheritance
class Motorcycle(Vehicle):
    def __init__(self, model, year, motoname, owner):
        super().__init__(model, year)
        self.name = motoname
        self.owner = owner
    
    #Polymorphism
    def accelerate(self):
        print("La moto está acelerando con su acelerador. ")

    def brake(self):
        print("La moto está frenando con sus frenos. ")

#Abstraction