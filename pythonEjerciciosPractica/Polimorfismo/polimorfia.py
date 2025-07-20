class Gato():
    def sonido(self):
        return "Miau"
    
class Perro():
    def sonido(self):
        return "Guau"    

def hacer_sonido(animal):
    print(animal.sonido())

gato = Gato()
perro = Perro()


#Forma uno de polimorfismo:
print(gato.sonido())
print(perro.sonido())

#Forma dos de polimorfismo:
hacer_sonido(gato)
hacer_sonido(perro)

