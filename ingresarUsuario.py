import tkinter as tk
from tkinter import Frame
from tkinter import messagebox
import baseDatos
 
window = tk.Tk()
window.title("Iniciar Sesion")
window.geometry("400x300")

def login():
    username=entradaUsuario.get()
    password=entradaClave.get()

    if baseDatos.ingresarUsuario(username,password):
        messagebox.showinfo("Mensaje","Bienvenido a la plataforma")
    else:
        messagebox.showinfo("Mensaje","Usuario o contraseña incorrectos")
    limpiarFormulario()
    
def limpiarFormulario():
    entradaUsuario.delete(0,tk.END)
    entradaClave.delete(0,tk.END)

frameLogin = Frame(window,bg="orange2")
frameLogin.pack(expand=True, fill="both")

etiquetaBienvenida = tk.Label(frameLogin,text = "Bienvenido\n Por favor", font= "arial",bg="orange2")
etiquetaBienvenida.place(x=150, y=5)

etiquetaUsuario = tk.Label (frameLogin,text = "Ingrese su usuario",bg="orange2")
etiquetaUsuario.place(x=30, y=100)


entradaUsuario = tk.Entry(frameLogin)
entradaUsuario.place(x=150, y=100)

etiquetaClave = tk.Label(frameLogin,text = "Ingrese su contraseña",bg="orange2")
etiquetaClave.place(x=30, y=150)

entradaClave = tk.Entry(frameLogin,show="*")
entradaClave.place(x=150,y=150)

botonLogin = tk.Button(frameLogin,text= "Ingresar", command= login,bg="green1")
botonLogin.place(x=160,y=200)

botnCrear = tk.Button(frameLogin,text= "Crear usuario",bg="green1")
botnCrear.place(x=150, y=230)


tk.mainloop()