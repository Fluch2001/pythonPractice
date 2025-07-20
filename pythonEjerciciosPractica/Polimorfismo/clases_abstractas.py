from abc import ABC, abstractmethod

class Persona(ABC):
    @abstractmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractmethod
    def trabajar(self):
        pass

    def presentarse(self):
        print(f"Hola, me llamo: {self.nombre} y tengo: {self.edad} años")

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def trabajar(self):
        print(f"Estoy estudiando {self.actividad}")

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def trabajar(self):
        print(f"Actualmente estoy trabajando en el rubro de: {self.actividad}")


francisco = Estudiante("Francisco", 23, "Masculino", "Programación")
francisco.presentarse()
francisco.trabajar()

diego = Trabajador("Diego", 20, "Masculino", "Programación")
diego.presentarse()
diego.trabajar()