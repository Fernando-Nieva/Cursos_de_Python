lenguajes = "Pyton ; Java; Ruby; PHP; Swift; JavaScript; C#; C; C++;"

separador = "; "
resultado = lenguajes.split(separador)# resultado e suna lista

# nuevo_string=" curso:".join(resultado)

nuevo_string=separador.join(resultado)

texto = """Este es un texto
con saltos
de 
linea
"""
resultado2 =texto.splitlines()

print(resultado)
print(resultado2)
print(nuevo_string)