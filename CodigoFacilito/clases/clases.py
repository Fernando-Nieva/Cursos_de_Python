
class Usuario:

    def __init__(self,username='',correo='',nombre=''):
        self.username =username
        self.correo =correo
        self.nombre =nombre

    def saluda(self):
        return ("Hola, soy el usuario"+" "+self. nombre)
    
    def mostrar_username(self):
        print(self.username)

    def mostrar_nombre(self):
        print(self.nombre)

    def crear_nombre(self,nombre):
        self.nombre = nombre

codi = Usuario("codi","codi@gmail.com","codigo")
facilito = Usuario()

# codi.username = 'codi'
# codi.correo = 'codi@gmail.com'

# facilito.username = 'Facilito'
# facilito.correo = 'facilito@gmail.com'

# print(type("codi"))
# print(type("facilito"))

# print(codi.saluda("codi"))
# print(facilito.saluda("facilito"))

# codi.mostrar_username()
# facilito.mostrar_username()

# codi.crear_nombre("Codigo")
# codi.mostrar_nombre()


resultado=codi.saluda()
print(resultado)