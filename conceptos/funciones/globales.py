animal= 'Leon' #Es una variable Global

def mostrar_animal():
    global animal #definir la variable como global
    animal='Ballena' #ES una variable local
    print(animal)

mostrar_animal()
print(animal)