#Codes Task

class Paradigmatico:    #Nomas andaba jugando
    def __init2__(self):
        print("Hola soy un objeto de un método dentro de una clase y soy tonto bla bla bla.")
        print("Perdón, cambié de propósito, ahora soy una librería.")

class Libros:   #Clases ya principal para definiar cada libro
    def __init__(self, titulo, autor, paginas, tipo):   #Pidiendo datos
        self.titulito = titulo  #Asignando datos
        self.autorsito = autor
        self.paginillas = paginas
        self.tipillos = tipo

    def checar(self):   #Método que me devuelve mis datos de manera bonita
        print(f"Titulo: {self.titulito}, Autor: {self.autorsito}, Páginas: {self.paginillas}, Género: {self.tipillos}.")

libroejemplo = Libros("Curso de cholo", "El Brayan", 15, "Enseñanza")   #Ejemplo propio
libroejemplo.checar()   #Revisando que si funciona mi método e hice bien todo hasta ahora

# Inherencia, esta clase está inherando desde la clase (Libros)
class Libreria(Libros):    #Segunda Clase basada en la inherencia pero con más cositas
    def __init__(self, titulo, autor, paginas, tipo):   #Realmente no agregué nada pero si creé más métodos
        super().__init__(titulo, autor, paginas, tipo)
        print(f"Titulo: {self.titulito}, Autor: {self.autorsito}, Páginas: {self.paginillas}, Género: {self.tipillos}.")
        self.total = 0

    # Abstracción, aquí encapsulé el checar cuantas páginas hay en total de todos los libros
    def checarpaginas(self):    #Método para checar el total de páginas    
        self.total += self.paginillas
        print(self.total)

# Polimorfismo, aquí lo apliqué llamando al metodo checar de la clase (Libros)
def chequeo(libronuevo): 
    libronuevo.checar()

Libro0 = Libros("Libro de Cocina", "David Hernández", 101, "Cocina")    #Ejemplo para polimorfismo
chequeo(Libro0)    #Ejecución de la función del poliformismo

libro1 = Libreria("Los Juegos del Hambre", "Suzane Collins", 384, "Ciencia ficción")    #Libros originales
libro1.checarpaginas()

libro2 = Libreria("Breve Historia del Tiempo", "Stephen Hawking", 256, "Cosmología")
libro1.checarpaginas()

libro3 = Libreria("Cien Años de Soledad", "Gabriel García Márquez", 432, "Realismo Mágico")
libro1.checarpaginas()

#Puse este porque pedía que se puedan agregar libros pero no encontré motivo de hacer otro método si ya con el incial se crean
Libro4 = Libreria(input(), input(), int(input()), input())