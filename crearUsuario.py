import tkinter as tk
import baseDatos 

ventana = tk.Tk()
ventana.title("ADM Usuarios")
ventana.geometry("450x400")

def limpiarFormulario():
    entradaNombre.delete(0,tk.END)
    entradaApellido.delete(0,tk.END)
    entradaUsuario.delete(0,tk.END)
    entradaNacimiento.delete(0,tk.END)
    entradaCorreo.delete(0,tk.END)
    entradaContrasenia.delete(0,tk.END)


def guardar():
    username = entradaUsuario.get()
    nombre = entradaNombre.get()
    apellido = entradaApellido.get()
    nacimiento = entradaNacimiento.get()
    correo = entradaCorreo.get()
    contrasenia = entradaContrasenia.get()

    baseDatos.guardarDatos(username,nombre,apellido,correo,nacimiento,contrasenia)

    limpiarFormulario()


etiquetaUsuario = tk.Label(text= "Usuario:")
etiquetaUsuario.place(x= 30, y= 50)

entradaUsuario = tk.Entry()
entradaUsuario.place(x= 150, y= 50)

etiquetaNombre = tk.Label(text= "Nombre:")
etiquetaNombre.place(x= 30, y= 100)

entradaNombre = tk.Entry()
entradaNombre.place(x= 150, y= 100)

etiquetaApellido = tk.Label(text= "Apellido:")
etiquetaApellido.place(x= 30, y= 150)

entradaApellido = tk.Entry()
entradaApellido.place(x= 150, y= 150)

etiquetaNacimiento = tk.Label(text= "Fecha Nacimiento:")
etiquetaNacimiento.place(x= 30, y= 200)

entradaNacimiento = tk.Entry()
entradaNacimiento.place(x= 150, y= 200)


etiquetaCorreo = tk.Label(text= "Correo Electronico:")
etiquetaCorreo.place(x= 30, y= 250)

entradaCorreo = tk.Entry()
entradaCorreo.place(x= 150, y= 250)


etiquetaContrasenia = tk.Label(text= "Contraseña:")
etiquetaContrasenia.place(x= 30, y= 300)

entradaContrasenia = tk.Entry(show = "*")
entradaContrasenia.place(x= 150, y= 300)


boton = tk.Button(text= "Guardar", command= guardar, bg = "green")
boton.place(x= 160, y= 350)


tk.mainloop()