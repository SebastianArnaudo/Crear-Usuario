import sqlite3


conet = sqlite3.connect("baseDeDatos")
cursor = conet.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS usuarios (id INTEGRES PRIMARY KEY AUTOINCREMENT NOT NULL, username VARCHAR(50) NOT NULL,nombre VARCHAR(50) NOT NULL, apellido VARCHAR(50) NOT NULL, email VARCHAR (50) NOT NULL UNIQUE, nacimiento VARCHAR(50) NOT NULL, password VARCHAR(40) NOT NULL)')

def guardarDatos(username,nombre,apellido,email,nacimiento,password):
    cursor.execute("INSERT INTO usuarios VALUES (NULL,?,?,?,?,?,?)",(username,nombre,apellido,email,nacimiento,password))
    conet.commit()


