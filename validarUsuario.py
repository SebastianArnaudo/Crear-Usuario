from tkinter import messagebox
from datetime import datetime
import re

def validarEmail(email):
 
  patron = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
  
  if re.match(patron, email):
  
    return True
  else:
    messagebox.showinfo("Aviso","Formato de correo invalido")



def validarNombre(usuario):
    if len(usuario) >= 4:
        return True
    else:
        messagebox.showinfo("Aviso","El nombre de Usuario no bede tener menos de 4 caracteres")

def validarClave(clave):
    if len(clave) >= 5:
        return True
    else:
        messagebox.showinfo("Aviso","La clave no debe tener menos de 5 caracteres")





def calculoEdad(dia,mes,ano):
    d=datetime.now()
    anoActual=d.year
    mesActual=d.month
    diaActual=d.day
    if mes==mesActual and dia>diaActual:
        edad=anoActual-ano-1
    elif mes>mesActual:
        edad=anoActual-ano-1
    else:
        edad=anoActual-ano

    return edad



def validarFecha(nacimiento):
  
  string=nacimiento
  lista=string.replace("-","/")
  barras=lista.count("/")
  
  if barras==2:
    lista=lista.split("/")
    try:
        edad=calculoEdad(int(lista[0]),int(lista[1]),int(lista[2]))
    
        if edad<0:
            messagebox.showinfo("Aviso","Segun la fecha,sted aun no ha nacido")
        else: 
            return True
    except:
        messagebox.showinfo("Aviso","Formato de fecha incorrecto")
  else:
     messagebox.showinfo("Aviso","Formato de fecha incorrecto")