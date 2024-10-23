
class Usuario:
    # metodo constructor
    __edad = 0
    def __init__(self,nombre):
        self._nombre = nombre

    def saludar(self,saludo):
        print(saludo+ self.nombre)

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self,valor):
        if(valor <0 ):
            raise ValueError ('Edad no puede ser menor que 0')
        self.__edad=valor
        

class Empleado(Usuario):
    __salario=0

    def modificar_salario(self,salario):#stter
        self.__salario = salario

    def ver_salario(self):#getter
        print(self.__salario)

def salduar(self):
    super.saludar("Hola")
    print("mi nombre es:"+self._nombre+"y gano:"+str(self.__salario))


empleado=Empleado("Fernando")
empleado.edad=32
print(empleado.edad)