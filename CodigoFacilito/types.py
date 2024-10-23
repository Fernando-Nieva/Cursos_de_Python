def saludo(nombre : str) -> None:
    print("Hola "+nombre)

def suma(num1 :int,num2:int = 100)->int:
    return num1+num2


nombre = "Eduardo"
saludo(nombre)

print(suma(10))


# Ventajas de Type Annotations:
# Mejor legibilidad: Otros desarrolladores pueden entender más fácilmente qué tipos de datos espera tu código.
# Verificación estática: Herramientas como mypy pueden analizar tu código antes de la ejecución para detectar errores de tipo.
# Autocompletado en editores: Los editores de código pueden ofrecer sugerencias más precisas basadas en los tipos anotados.