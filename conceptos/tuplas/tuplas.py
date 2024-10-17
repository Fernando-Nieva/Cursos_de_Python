# tupla = (1,2,3,4,5,6,7,8,9,0)

# elemento = tupla [-4]
# sub = tupla [:9:2]
# print(elemento)
# print(sub)

# tupla = (1,2,3,4,5,6)

# uno,dos,tres,*cuatro = tupla
# uno,*dos,cinco,seis = tupla
# print(uno)
# print(dos)
# print(cinco)
# print(seis)

tupla = (1,2,3,4,5,6)
tupla_dos = (100,200,300,400)
lista=[10,20,30,40]

resultado = zip(tupla , lista,tupla_dos)
# resultado = tuple(resultado)
resultado = list(resultado)
print(resultado)