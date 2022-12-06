from tkinter import messagebox


def validarNombre(usuario):
    if len(usuario) < 4:
        messagebox.showinfo("Aviso","El nombre de Usuario no bede tener menos de 4 caracteres")

def validarClave(clave):
    if len(clave) < 5:
        messagebox.showinfo("Aviso","La clave no debe tener menos de 5 caracteres")




def validarFecha(fecha):
    string=fecha
    lista=string.replace("-","/")
    barras=lista.count("/")
    if barras==2:
        lista=lista.split("/")
    else:
        messagebox.showinfo("Aviso","Formato de fecha Incorrecto")