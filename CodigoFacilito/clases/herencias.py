class Animal:
    def comer(self):
        print("comiendo")
    def durmiendo(self):
        print("durmiendo")

    def comun(self):
        print("Este e sun metodo de Animal")

class Mascota:
    def __init__(self, nombre, fecha):
        self.nombre = nombre
        self.fecha_de_adopcion = fecha
        
    def comun(self):
        print("Este e sun metodo de mascota")


class Perro(Animal, Mascota):
    def __init__(self, nombre, fecha):
        # Llamar al constructor de Mascota
        Mascota.__init__(self, nombre, fecha)
    
    def ladra(self):
        print("ladrando")       

    def comun(self):
        print("Este es sun metodo de perro")
    
    def durmiendo(self): #sobre escritura d emetodo
        print(self.nombre," esta durmiendo")
        Animal.durmiendo(self)
        print("No molestar")

class Gato(Animal, Mascota):
    def __init__(self, nombre, fecha):
        # Llamar al constructor de Mascota
        Mascota.__init__(self, nombre, fecha)
    
    def ronroneo(self):
        print("ronroneando")

# Creación de la instancia
firulais = Perro("Firulais", "18-10-24")
print ("Adopcion:",firulais.fecha_de_adopcion)
firulais.ladra()
firulais.comer()
firulais.durmiendo()
firulais.comun()
