class Numero:
    def __init__(self, value):
        self.value = value

    def compare(self, numero):
        if numero.value > self.value:
            return numero.value
        return self.value

   
class Cadena:
      
      def __init__(self, value):
        self.value = value

      def compare(self,cadena):
        palabras = [self.value,cadena.value]
        palabras.sort()
        return palabras[0]
   

class Lista:
   
   def __init__(self,value):
    self.value = value
   
   def compare(self,lista): 
      if len(self.value)>len(lista.value):
         return self.value
      return lista.value
      


def retornaElMayor(a,b):
   return a.compare(b)



numero_uno = Numero(10)
numero_dos = Numero(2)

cadena_uno = Cadena("fernando")
cadena_dos =Cadena("uriel")


lista_uno =Lista([1,2])
lista_dos =Lista([1,2,3,4,5])
# print(retornaElMayor(numero_uno,numero_dos))
# print(retornaElMayor(cadena_uno,cadena_dos))
print(retornaElMayor(lista_uno,lista_dos))


# def retornaElMayora(a,b):
#     #instancia
#     if isinstance(a,int) and isinstance(b,int):
#        if a > b:
#         return a
#        return b
#     if isinstance(a,str) and isinstance (b,str):
#         palabras= [a,b]
#         palabras.sort()
#         return palabras[0]
#     if isinstance(a,list) and isinstance (b,list):
#        if len (a) > len (b):
#           return a
#        return b
# # print(retornaElMayora("uriel","alejandro"))
# print(retornaElMayora([1,2,3],[1,2,3,4])) 