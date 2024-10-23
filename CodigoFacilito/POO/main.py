# class Curso:
#     pass

# # instancia de Curso
# curso_python=Curso()


class Usuario:
    nombre ="Uriel"

    # metodo constructor
    def __init__(self,nombre):
        self._nombre = nombre

    def saludar(self,saludo):
        print(saludo+ self.nombre)


uriel=Usuario("Marcos")
uriel.email ="uriel@gmail.com"

cody=Usuario("pepe")


# cody.nombre="Cody"


# uriel.saludar()
# cody.saludar()
# print(uriel.nombre)
# print(cody.nombre)

# herencia

class Empleado(Usuario):
    
    __salario = 0
    
    def modificar_salario(self,salario):
        self.__salario =salario
        

    def ver_salario(self):
        print("salario:",self.__salario)


    def saludar(self):
        super().saludar("Hola!")
        print("Mi nombre es:"+self.nombre+" y gano:"+str(self.__salario))

empleado = Empleado("Uriel")
# empleado.saludar()
empleado.modificar_salario(1000)
empleado.ver_salario()

print(empleado.__salario)
# empleado.saludar()

empleado=Empleado("juan")
print(empleado._nombre)

class Pagina:
    def imprimir_pie_pagina(self):
        print(self.pie_pagina)


class PaginaLegal(Pagina):
    def imprimir_pie_pagina(self):
        super().imprimir_pie_pagina()
        print("Derechos reservados")



html = PaginaLegal()
html.pie_pagina="<p>Hola</p>"

html.imprimir_pie_pagina()