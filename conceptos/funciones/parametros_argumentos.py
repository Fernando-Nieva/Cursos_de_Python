

def crear_usuario(nombre,apellido,edad=16):
    return{
        'nombre':nombre,
        'apellido':apellido,
        'nombre_completo':"{}{}".format(nombre,apellido),
        'edad':edad
    }

codi=crear_usuario("codi","facilito",)
print(codi["nombre"])
print(codi["apellido"])
print(codi["edad"])