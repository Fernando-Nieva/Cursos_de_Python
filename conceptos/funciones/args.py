# def suma (val1,val2,val3):
#     return val1+val2+val3

# def suma (parametreo_requerido,*args):
#     total = 0
#     print(parametreo_requerido)
#     for valor in args:
#         total+=valor
#     return total

# resultado = suma("Este es un parametro requerido",10,20,30,40,10,50,5)
# print(resultado)

# Función que suma todos los valores después del primer parámetro requerido
def suma(parametro_requerido, *args):
    print(parametro_requerido)  # Muestra el parámetro requerido
    return sum(args)  # Suma todos los valores en *args y los retorna

# Función que imprime los usuarios autenticados utilizando **kwargs
def usuarios_autenticados(**kwargs):
    print(kwargs)

# Ejecuta la función suma
resultado = suma("Este es un parámetro requerido", 10, 20, 30, 40, 10, 50, 5)
print(resultado)  # Muestra el resultado de la suma

# Función que acepta un parámetro requerido, *args y **kwargs
def combinacion(requerido, *args, **kwargs):
    print(requerido)  # Muestra el valor requerido
    print(args)  # Muestra los argumentos no nombrados
    print(kwargs)  # Muestra los argumentos nombrados

# Ejecuta la función combinacion
combinacion("valor requerido", 10, 20, valor_uno=True, valor_dos=False)
