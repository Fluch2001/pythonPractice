def decorador(funcion):
    def funcion_modificada():
        print("Ejemplo")
        funcion()
    return funcion_modificada

# class Miclase:
#     def __init__(self):
#         self._atributo_privado = "Valor"

@decorador
def saludo():
    print("Hola")

saludo()