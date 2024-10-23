class FilaBanco:
    def __init__(self):
        self.usuarios = Queue()  # Inicializamos un hash de usuarios

    def siguiente_usuario(self, numero):
        # Implementación: obtenemos el siguiente usuario con el número de turno
        return self.usuarios.obtener(numero)

    def formar_usuario(self, numero, usuario):
        # Agregamos el usuario con el número de turno al hash
        self.usuarios.agregar(numero, usuario)


class Hash:
    def __init__(self):
        # Inicializamos el diccionario vacío
        self.data = {}

    def obtener(self, llave):
        # Retornamos el valor asociado a la llave, si no existe retorna None
        return self.data.get(llave, None)

    def agregar(self, llave, valor):
        # Asignamos un valor a una llave específica
        self.data[llave] = valor


class Queue:
    def __init__(self):
        # Inicializamos la cola como una lista vacía
        self.data = []

    def obtener(self):
        # Si la cola no está vacía, retornamos el primer elemento (FIFO)
        if self.data:
            return self.data.pop(0)  # pop(0) simula comportamiento de cola
        return None

    def agregar(self, valor):
        # Agregamos un valor al final de la cola
        self.data.append(valor)
