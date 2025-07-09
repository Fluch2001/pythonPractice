# Importar Bibliotecas
from tkinter import *
from tkinter import ttk, messagebox, PhotoImage
from mensaje import *
from gestor import *
from empleado import *
#################################### Invocar metodos para BD #####################################
def conexionBBDD():
	gestor.conexionBBDD()

def eliminarBBDD():
	gestor.eliminarBBDD()	
	limpiarMostrar()

def limpiarCampos():
	miId.set("") 
	miNombre.set("")
	miCargo.set("")
	miSalario.set("")

def limpiarMostrar():
	limpiarCampos()
	mostrar()

def mostrar():
	gestor.mostrar(tree)

def salirAplicacion():
	valor=messagebox.askquestion("Salir",mensaje.SALIR)
	root.destroy() if valor=="yes" else None

######################################## Invocar metodos CRUD ##############################################
def crear(nombre, cargo, salario):
    miConexion, miCursor = servicio.conectar()
    empleado_obj = empleado(nombre, cargo, salario)
    miCursor.execute(consulta.insert, empleado_obj.info())
    miConexion.commit()
		
def actualizar():
	gestor.actualizar(miNombre.get(), miCargo.get(), miSalario.get(), miId.get())
	limpiarMostrar()		

def buscar():
	gestor.search(tree, miNombre.get())

def borrar():
    gestor.delete(miId.get())
    limpiarMostrar()

def seleccionarUsandoClick(event):
	item=tree.identify('item',event.x,event.y)
	miId.set(tree.item(item,"text"))
	miNombre.set(tree.item(item,"values")[0])
	miCargo.set(tree.item(item,"values")[1])
	miSalario.set(tree.item(item,"values")[2])


# Desarrollo de la Interfaz grafica
root=Tk()
root.title("Aplicación CRUD con Base de Datos")
root.configure(background='lightblue')
root.geometry("600x350")

#iconos

imagenBuscar = PhotoImage(file="imagenes/buscar.png")
imagenCrear = PhotoImage(file="imagenes/crear.png")
imagenMostrar = PhotoImage(file="imagenes/mostrar.png")
imagenActualizar = PhotoImage(file="imagenes/actualizar.png")
imagenEliminar = PhotoImage(file="imagenes/eliminar.png")


#Variables cajas de texto
miId=StringVar()
miNombre=StringVar()
miCargo=StringVar()
miSalario=StringVar()



                ################################## Tabla ################################
tree=ttk.Treeview(height=10, columns=('#0','#1','#2'))
tree.place(x=0, y=130)
tree.column('#0',width=100)
tree.heading('#0', text="ID", anchor=CENTER)
tree.heading('#1', text="Nombre del Empleado", anchor=CENTER)
tree.heading('#2', text="Cargo", anchor=CENTER)
tree.column('#3', width=100)
tree.heading('#3', text="Salario", anchor=CENTER)
tree.bind("<Button-1>", seleccionarUsandoClick)
mostrar()


#Widgets

###################### Colocar widgets en la VISTA ######################
########## Creando Los menus ###############
menubar=Menu(root)
menubasedat=Menu(menubar,tearoff=0)
menubasedat.add_command(label="Crear/Conectar Base de Datos", command=conexionBBDD)
menubasedat.add_command(label="Eliminar Base de Datos", command=eliminarBBDD)
menubasedat.add_command(label="Salir", command=salirAplicacion)
menubar.add_cascade(label="Inicio", menu=menubasedat)

ayudamenu=Menu(menubar,tearoff=0)
ayudamenu.add_command(label="Resetear Campos", command=limpiarCampos)
ayudamenu.add_command(label="Acerca", command=gestor.mensaje)
menubar.add_cascade(label="Ayuda",menu=ayudamenu)

############## Creando etiquetas y cajas de texto ###########################
e1=Entry(root, textvariable=miId)

l2=Label(root, text="Nombre", background='lightblue').place(x=50,y=10)
e2=Entry(root, textvariable=miNombre, width=50)
e2.place(x=100, y=10)

l3=Label(root, text="Cargo", background='lightblue').place(x=50,y=40)
e3=Entry(root, textvariable=miCargo)
e3.place(x=100, y=40)

l4=Label(root, text="Salario", background='lightblue').place(x=280,y=40)
e4=Entry(root, textvariable=miSalario, width=10)
e4.place(x=320, y=40)

l5=Label(root, text="USD", background='lightblue').place(x=380,y=40)

################# Creando botones ###########################



b0 = Button(root, image=imagenBuscar, command=buscar)
b0.place(x=450, y=10)

b1=Button(root, image=imagenCrear, bg="green", command=crear).place(x=50, y=85)
b2=Button(root, image=imagenActualizar, bg="yellow", command=actualizar).place(x=180, y=85)
b3=Button(root, image=imagenMostrar, bg="yellow", command=mostrar).place(x=320, y=85)
b4=Button(root, image=imagenEliminar,bg="#df004a", command=borrar).place(x=450, y=85)


root.config(menu=menubar)


root.mainloop()

