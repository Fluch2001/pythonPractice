from tkinter import messagebox
from mensaje import *
from servicio import *
from empleado import *

class gestor:

    # Gestionar servicios de conexión
    @staticmethod
    def conexionBBDD():
        try:
            servicio.conexionBBDD()
            messagebox.showinfo("Conexión", mensaje.EXITO_BD)
        except:
            messagebox.showinfo("Conexión", mensaje.ERROR_BD)

    @staticmethod
    def eliminarBBDD():
        if messagebox.askyesno(message=mensaje.CONFIRMAR_BD, title="Advertencia"):
            servicio.eliminarBBDD()
        else:
            messagebox.showinfo("Conexión", mensaje.ERROR_ELIMINAR_BD)

    # Gestionar servicios CRUD empleados

    @staticmethod
    def mostrar(tree):
        registros = tree.get_children()
        [tree.delete(elemento) for elemento in registros]

        try:
            empleados = servicio.consultarBBDD()
            for row in empleados:
                tree.insert("", 0, text=row[0], values=(row[1], row[2], row[3]))
        except:
            messagebox.showwarning("Advertencia", mensaje.ERROR_MOSTRAR)

    @staticmethod
    def search(tree, criterio):
        registros = tree.get_children()
        [tree.delete(elemento) for elemento in registros]

        try:
            if criterio != "":
                empleados = servicio.search(criterio)
                for row in empleados:
                    tree.insert("", 0, text=row[0], values=(row[1], row[2], row[3]))
            else:
                messagebox.showwarning("Advertencia", mensaje.NOMBRE_FALTANTE)
        except:
            messagebox.showwarning("Advertencia", mensaje.ERROR_BUSCAR)

    @staticmethod
    def crear(nombre, cargo, salario):
        try:
            if nombre != "" and cargo != "" and salario != "":
                servicio.crear(nombre, cargo, salario)
            else:
                messagebox.showwarning("Advertencia", mensaje.CAMPOS_FALTANTES)
        except:
            messagebox.showwarning("Advertencia", mensaje.ERROR_CREAR)

    @staticmethod
    def actualizar(nombre, cargo, salario, id):
        try:
            if nombre != "" and cargo != "" and salario != "":
                servicio.actualizar(nombre, cargo, salario, id)
            else:
                messagebox.showwarning("Advertencia", mensaje.CAMPOS_FALTANTES)
        except:
            messagebox.showwarning("Advertencia", mensaje.ERROR_ACTUALIZAR)

    @staticmethod
    def delete(id):
        if messagebox.askyesno(message=mensaje.CONFIRMAR, title="Advertencia"):
            servicio.borrar(id)
        else:
            messagebox.showwarning("Advertencia", mensaje.ERROR_ELIMINAR)

    # Información de la aplicación

    @staticmethod
    def mensaje():
        messagebox.showinfo(title="Información", message=mensaje.ACERCA)
