import tkinter as tk
import baseDatos 
import base64
from validarUsuario import validarClave,validarFecha,validarNombre,validarEmail
from tkinter import Frame
from tkinter import messagebox




def main():
    
    ventana = tk.Tk()
    ventana.title("ADM Usuarios")
    ventana.geometry("450x450")


    def ingresar():


        window= tk.Toplevel()
        window.title("Iniciar Secion")
        window.geometry("400x300")
        
       

        def login():
            username=entradaUsuario.get()
            password=entradaClave.get()
            password = password.encode("ascii")
            password=base64.b64encode(password)


            if baseDatos.ingresarUsuario(username,password):
                messagebox.showinfo("Mensaje","Bienvenido Usuario")
            else:
                messagebox.showinfo("Mensaje","Usuario o contraseña incorrectos")
            limpiarFormulario()

        frameLogin = Frame(window,bg="orange2")
        frameLogin.pack(expand=True, fill="both")

        etiquetaBienvenida = tk.Label(window,text = "Bienvenido\n Por favor", font= "arial",bg="orange2")
        etiquetaBienvenida.place(x=150, y=5)

        etiquetaUsuario = tk.Label (window,text = "Ingrese su usuario",bg="orange2")
        etiquetaUsuario.place(x=30, y=100)


        entradaUsuario = tk.Entry(window)
        entradaUsuario.place(x=150, y=100)

        etiquetaClave = tk.Label(window,text = "Ingrese su contraseña",bg="orange2")
        etiquetaClave.place(x=30, y=150)

        entradaClave = tk.Entry(window,show="*")
        entradaClave.place(x=150,y=150)

        botonLogin = tk.Button(window,text= "Ingresar", command= login,bg="green1")
        botonLogin.place(x=160,y=200)

       
            




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
        
        contrasenia = contrasenia.encode("ascii")
        contrasenia=base64.b64encode(contrasenia)


        if validarEmail(correo) and validarNombre(username) and validarClave(contrasenia) and validarFecha(nacimiento):

            baseDatos.guardarDatos(username,nombre,apellido,correo,nacimiento,contrasenia)
            messagebox.showinfo("Usuario Guardado","El usuario fue guardado con exito")
            limpiarFormulario()

        else:
            messagebox.showinfo("Aviso","El usuario no pudo ser guardado")


        

    framePrincipal = Frame(ventana, bg="gray")
    framePrincipal.pack(expand=True,fill="both")

    eBienvenida = tk.Label(framePrincipal,text = "Por favor\n Cree un usuario", font= "arial",bg="gray")
    eBienvenida.place(x=150, y =5)

    etiquetaUsuario = tk.Label(framePrincipal,text= "Usuario:",bg="gray")
    etiquetaUsuario.place(x= 30, y= 50)

    entradaUsuario = tk.Entry(framePrincipal)
    entradaUsuario.place(x= 150, y= 50)

    etiquetaNombre = tk.Label(framePrincipal,text= "Nombre:",bg="gray")
    etiquetaNombre.place(x= 30, y= 100)

    entradaNombre = tk.Entry(framePrincipal)
    entradaNombre.place(x= 150, y= 100)

    etiquetaApellido = tk.Label(framePrincipal,text= "Apellido:",bg="gray")
    etiquetaApellido.place(x= 30, y= 150)

    entradaApellido = tk.Entry(framePrincipal)
    entradaApellido.place(x= 150, y= 150)

    etiquetaNacimiento = tk.Label(framePrincipal,text= "Fecha Nacimiento:",bg="gray")
    etiquetaNacimiento.place(x= 30, y= 200)
    eAclaracionFecha = tk.Label(framePrincipal, text= "* En formato\n DD/MM/AAA", bg="grey")
    eAclaracionFecha.place(x=300,y=200)

    entradaNacimiento = tk.Entry(framePrincipal)
    entradaNacimiento.place(x= 150, y= 200)


    etiquetaCorreo = tk.Label(framePrincipal,text= "Correo Electronico:",bg="gray")
    etiquetaCorreo.place(x= 30, y= 250)

    entradaCorreo = tk.Entry(framePrincipal)
    entradaCorreo.place(x= 150, y= 250)


    etiquetaContrasenia = tk.Label(framePrincipal,text= "Contraseña:",bg="gray")
    etiquetaContrasenia.place(x= 30, y= 300)

    entradaContrasenia = tk.Entry(framePrincipal,show = "*")
    entradaContrasenia.place(x= 150, y= 300)


    boton = tk.Button(framePrincipal,text= "Guardar", command= guardar,bg = "green1")
    boton.place(x= 170, y= 350)





    botonI = tk.Button(framePrincipal, text="Iniciar Secion", command= ingresar, bg="blue1", fg="white")
    botonI.place(x=165,y=380)


    tk.mainloop()
if __name__== "__main__":
    main()