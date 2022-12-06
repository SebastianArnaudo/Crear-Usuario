import tkinter as tk
from tkinter import Frame
from tkinter import messagebox
import baseDatos
 
window = tk.Tk()
window.title("Iniciar Sesion")
window.geometry("400x300")

def login():
    username=usuarioI.get()
    password=claveI.get()

    if baseDatos.ingresarUsuario(username,password):
        messagebox.showinfo("Mensaje","Bienvenido a la plataforma")
    else:
        messagebox.showinfo("Mensaje","Usuario o contraseña incorrectos")
    limpiarFormulario()
    
def limpiarFormulario():
    usuarioI.delete(0,tk.END)
    claveI.delete(0,tk.END)

etiquetaBienvenida = tk.Label(text = "Bienvenido\n Por favor", font= "arial")
etiquetaBienvenida.pack()

etiquetaUsuario = tk.Label (text = "Ingrese su usuario")
etiquetaUsuario.pack()


usuarioI = tk.Entry()
usuarioI.pack()

etiquetaClave = tk.Label(text = "Ingrese su contraseña")
etiquetaClave.pack()

claveI = tk.Entry()
claveI.pack()

bLogin = tk.Button(text= "Ingresar", command= login)
bLogin.pack()


tk.mainloop()