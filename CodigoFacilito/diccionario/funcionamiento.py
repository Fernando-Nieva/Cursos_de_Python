# diccionario ={}
# diccionario ["nombre"]="codi"

# valor = diccionario["nombre"]
# diccionario["nombre"]=960
# print(diccionario)
# print(valor)

diccionario ={"a":1,"b":2,"c":3,"a":4,"d":5}
# resultado = "a" in diccionario
# resultado = diccionario.get ("z","la llave no existe")
# resultado = diccionario.setdefault ("z",{})
# resultado = diccionario.keys ()
# resultado = diccionario.values ()
# resultado = diccionario.items()
# resultado = tuple(resultado)


# print(diccionario)
# print(resultado)

del diccionario["b"]
valor = diccionario.pop("c")
# diccionario.clear()


print(valor)
print(len (diccionario))
print(diccionario)