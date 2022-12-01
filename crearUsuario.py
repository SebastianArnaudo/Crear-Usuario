import tkinter as tk

ventana = tk.Tk()
ventana.title("ADM Usuarios")
ventana.geometry("450x400")

tituloMenu = tk.Label(text = "ABM Usuario", font="arial")
tituloMenu.place(x= 150, y= 10)


etiquetaNombre = tk.Label(text= "Nombre:")
etiquetaNombre.place(x= 30, y= 50)

entradaNombre = tk.Entry()
entradaNombre.place(x= 150, y= 50)

etiquetaApellido = tk.Label(text= "Apellido:")
etiquetaApellido.place(x= 30, y= 100)

entradaApellido = tk.Entry()
entradaApellido.place(x= 150, y= 100)

etiquetaNacimiento = tk.Label(text= "Fecha Nacimiento:")
etiquetaNacimiento.place(x= 30, y= 150)

entradaNacimiento = tk.Entry()
entradaNacimiento.place(x= 150, y= 150)


etiquetaCorreo = tk.Label(text= "Correo Electronico:")
etiquetaCorreo.place(x= 30, y= 200)

entradaCorreo = tk.Entry()
entradaCorreo.place(x= 150, y= 200)


etiquetaContrasenia = tk.Label(text= "contraseña:")
etiquetaContrasenia.place(x= 30, y= 250)

entradaContrasenia = tk.Entry()
entradaContrasenia.place(x= 150, y= 250)


boton = tk.Button(text= "Guardar")
boton.place(x= 160, y= 300)


tk.mainloop()