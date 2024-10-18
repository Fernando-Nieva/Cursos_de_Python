class Triangulo:

    numero =2

    @staticmethod
    def area(base,altura):
     return(base * altura)/ Triangulo.numero
    
# triangulo = Triangulo()
# triangulo.base = 10
# triangulo.altura = 20

resultado = Triangulo.area(10,20)
print(resultado)