
# def saluda():
#     print("Hola Miguel")

# saluda()

def crear_mensaje(nombre):
    return "Hola {}, bienvenido al curso de python3".format(nombre)
    

def suma(val1,val2,val3):
    return val1+val2+val3


def obtener_curso():
    return "Curso de Python","Basico",3.6


mensaje_nuevo = crear_mensaje("Eduardo")
print(mensaje_nuevo)

resultado = suma(10,20,30)
print(resultado)

curso,nivel,version = obtener_curso()
print(curso,nivel,version)
