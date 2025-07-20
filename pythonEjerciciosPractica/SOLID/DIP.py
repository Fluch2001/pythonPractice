class Diccionario:
    def verificar_palabra(self, palabra):
        #Logica para verificar palabras
        pass

class CorrectorOrtografico:
    def __init__(self):
        self.diccionario = Diccionario()

    def corregir_texto(self, texto):
        #Usamos el diccionario para corregir el texto
        pass

from abc import ABC, abstractmethod

class Verificador_ortografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        #Logica para verificar palabras
        pass

class Diccionario(Verificador_ortografico):
    def verificar_palabra(self, palabra):
        #Logica para verificar palabras si esta en el diccionario
        pass

class Servicio_online(Verificador_ortografico):
    def verificar_palabra(self, palabra):
        #Logica para verificar palabras desde el servicio web
        pass

class Corrector_ortografico:
    def __init__(self,verificador):
        self.verificador = verificador

    def corregir_texto(self, texto):
        #Usamos el verificador para corregir texto
        

corrector = Corrector_ortografico(Servicio_online())
