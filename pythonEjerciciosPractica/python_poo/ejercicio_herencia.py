#Ejercicio uno

#Crear un sistema para una escuela. Vamos a tener dos clases principales: *Persona* y *Estudiante*
#La clase Persona tendrá los atributos de nombre y edad junto a un método que imprima el nombre y la edad de la persona.
#La clase Estudiante heredará de la clase Persona y también tendrá un atributo adicional: Grado y un método que imprima el grado del estudiante.

#Deberás utilizar super en el método de inicialización (init) para reutilizar el codigo de la clase padre.
#Luego crea una instancia de la clase Estudiante e imprime sus atributos y utiliza sus métodos para asegurarte de que todo funcione correctamente.

#---------------------------------------------------------------------------------------------------------------------------#

#Resolución 

class Persona:
  def __init__(self,nombre,edad):
    self.nombre = nombre
    self.edad = edad

  def mostrar_datos(self):
    print(f"Nombre: {self.nombre}")
    print(f"Edad: {self.edad}")

class Estudiante(Persona):
  def __init__(self, nombre, edad, grado):
    super().__init__(nombre, edad)
    self.grado = grado

  def mostrar_grado(self):
    print(f"Grado: {self.grado}")


estudiante = Estudiante("Juan", "24", "6to")
estudiante.mostrar_datos()
estudiante.mostrar_grado()
