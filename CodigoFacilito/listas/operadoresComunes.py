
lista = [8.17,90,1,5,44,5,1.32]

# lista.sort()
lista.sort(reverse = True)
mayor = lista[0]
menor= min(lista)
longitud = len (lista)

resultado = 8.17 in lista

indice = lista.index(5)
contador = lista.count(5)

print(lista)
print(mayor)
print(menor)
print(longitud)
print(resultado)
print(indice)
print(contador)