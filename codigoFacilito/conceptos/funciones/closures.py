
def mostrar_mensaje(mensaje):
    mensaje = mensaje.title()#local

    def mostrar():
        print(mensaje)
    

    return mostrar

nueva_funcion = mostrar_mensaje("codigo Facilito")

nueva_funcion()



def crear_multiplicador(factor):
    def multiplicar(numero):
        return numero * factor  # 'factor' es recordado del entorno externo
    return multiplicar  # Devuelve la función 'multiplicar'

# Crear un closure que multiplica por 3
multiplicador_por_3 = crear_multiplicador(3)

# Usar el closure
resultado = multiplicador_por_3(10)
print(resultado)  # Imprime: 30
