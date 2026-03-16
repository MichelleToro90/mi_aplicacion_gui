class GestorDatos:

    def __init__(self):
        self.personas = []

    def agregar(self, nombre, cedula):
        persona = {
            "nombre": nombre,
            "cedula": cedula
        }
        self.personas.append(persona)

    def limpiar(self):
        self.personas.clear()

    def obtener_datos(self):
        return self.personas