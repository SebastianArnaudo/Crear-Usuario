import tkinter as tk
from tkinter import Frame
from tkinter import messagebox
import baseDatos
import base64
 
window = tk.Tk()
window.title("Iniciar Sesion")
window.geometry("400x300")

def login():

    def bienvenido():
        pagina = tk.Toplevel()
        pagina.title("Bienvenido")
        pagina.geometry("400x300")

        framePagina= Frame(pagina,bg="yellow")
        framePagina.pack(expand=True, fill="both")

        etiquetaIngresar = tk.Label(pagina, text="Bienvenido a la plataforma", font="arial",bg="yellow", fg=  "red")
        etiquetaIngresar.place(x=100, y=150)

    username=entradaUsuario.get()
    password=entradaClave.get()
    password = password.encode("ascii")
    password=base64.b64encode(password)


    if baseDatos.ingresarUsuario(username,password):
        bienvenido()
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



tk.mainloop()