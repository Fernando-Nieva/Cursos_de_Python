texto = "   curso de Python 3,Python basico   "

# resultado = texto.capitalize()
# resultado = texto.swapcase()
# resultado = texto.upper()
# resultado = texto.lower()
# resultado = texto.lower()
# resultado = texto.title()
# resultado = texto.replace("Python","ruby",1)
resultado = texto.strip()
# print(resultado.islower())
# print(resultado.isupper())
print(resultado)

curso = "Python"

version = "3"

# resultado2 = "Curso de %s %s "%(curso,version)
resultado2 = "Curso de {a} {b}".format(a=curso,b=version)
print(resultado2)

texto= "curso de Python"

texto = "c"+ curso[1:]+str(3) + " " + "en codigo facilito"

print(texto)

mensaje = "Este es un texto un pco grande en cuanto a longitud de caracteres se refiere"

# resultado3 = mensaje.count("z")
# resultado3 = "texto" in mensaje
# resultado3 = mensaje.find("texto")
# resultado3 = mensaje [resultado3: resultado3 +len("texto")]

# resultado3 = mensaje.startswith("Este")
resultado3 = mensaje.endswith("e")
print(resultado3)