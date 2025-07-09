class empleado:
    #constructor
    def __init__(self, nombre, cargo, salario):
        self.__nombre = nombre
        self.__cargo = cargo
        self.__salario = salario

    #retornar informacion del empleado
    def info(self):
        return self.__nombre, self.__cargo, self.__salario
    

#Test de la clase empleado

#empleado = empleado("Francisco", "IT Analyst", 2500)
#print(empleado.info())


