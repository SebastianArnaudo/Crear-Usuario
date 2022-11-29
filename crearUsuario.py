import tkinter as tk

ventana = tk.Tk()
ventana.title("ADM Usuarios")
ventana.geometry("450x400")

tituloMenu = tk.Label(text = "ABM Usuario", font="arial")
tituloMenu.place(x= 150, y= 10)

etiquetaCorreo = tk.Label(text= "Correo Electronico:")
etiquetaCorreo.place(x= 30, y= 50)

entradaCorreo = tk.Entry()
entradaCorreo.place(x= 150, y= 50)

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


boton = tk.Button(text= "Guardar")
boton.place(x= 160, y= 250)


tk.mainloop()