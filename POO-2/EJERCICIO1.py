print ("Martínez Estrada Ricardo / NO. de control: 1193 / 20-11-2024")
print (" ")

class Persona:
    # Clase que representa a una persona con nombre, edad y DNI.

    def __init__(self, nombre='', edad=0, dni=''):
        # Constructor que inicializa los atributos de la persona. Los datos son opcionales.
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        # Valida que el nombre sea una cadena no vacía.
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre debe ser una cadena no vacía.")
        self._nombre = valor.strip()

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        # Valida que la edad sea un número entero positivo.
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("La edad debe ser un número entero positivo.")
        self._edad = valor

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, valor):
        # Valida que el DNI sea una cadena válida.
        if not isinstance(valor, str) or len(valor) < 7:
            raise ValueError("El DNI debe tener al menos 7 caracteres.")
        self._dni = valor.strip()

    def mostrar(self):
        # Muestra los datos de la persona.
        return f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}"

    def esMayorDeEdad(self):
        # Devuelve True si la persona es mayor de edad.
        return self.edad >= 18