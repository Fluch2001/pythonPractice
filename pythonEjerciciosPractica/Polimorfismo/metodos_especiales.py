#Crear un juego de fusión.

#El juego consiste en crear personajes y que esos personajes se puedan fusionar para formar personajes mas poderosos que tengan más poder.

# para ello debemos cambiar el comportamiento del operador "+" para que cuando los personajes se fusionen, salga un nuevo personaje con habilidades mejoradas.

# una posible formula es: el promedio de las habilidades de ambos al cuadrado.

class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    def __repr__(self):
        return f"{self.nombre} (Fuerza: {self.fuerza}, Velocidad: {self.velocidad})"
    
    def __add__(self, otro_pj):
        nuevo_nombre = self.nombre + "-" + otro_pj.nombre
        nueva_fuerza = round(((self.fuerza + otro_pj.fuerza)/2)**1.5)
        nueva_velocidad = round(((self.velocidad + otro_pj.velocidad)/2)**1.5)
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)


vegeta = Personaje("Vegeta", 100, 100)
goku = Personaje("Goku", 99, 99)
jiren = Personaje("Jiren", 120, 120)


gogeta = vegeta + goku
jireta = jiren + gogeta

print(gogeta)
print(jireta)