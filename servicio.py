import sqlite3
from consulta import *
from empleado import *

class servicio:
    def conectar():
        miConexion = sqlite3.connect("base")
        miCursor = miConexion.cursor()
        return miConexion, miCursor
    
    def conexionBBDD():
        miConexion, miCursor = servicio.conectar()
        miCursor.execute(consulta.createTable)

    def eliminarBBDD():
        miConexion, miCursor = servicio.conectar()
        miCursor.execute(consulta.deleteTable)

    def consultarBBDD():
        miConexion, miCursor = servicio.conectar()
        miCursor.execute(consulta.select)
        return miCursor.fetchall()
    
    def crear():
        miConexion, miCursor = servicio.conectar()
        empleado=empleado(nombre, cargo, salario)
        miCursor.execute(consulta.insert, (empleado.info()))
        miConexion.commit()

    def actualizar(nombre, cargo, salario, id):
        miConexion, miCursor = servicio.conectar()
        empleado = empleado(nombre, cargo, salario)
        miCursor.execute(consulta.update+id, (empleado.info()))
        miConexion.commit()

    def borrar(id):
        miConexion, miCursor = servicio.conectar()
        miCursor.execute(consulta.delete+id)
        miConexion.commit()

    def search(nombre):
        miConexion, miCursor = servicio.conectar()
        miCursor.execute(consulta.search, (nombre,))
        miConexion.commit()
        return miCursor.fetchall()