
import sqlite3
import os

"""
clientes
    ESTO ES UNA TABLA
id nombre telefono correo
1 darius 45448646 dar@gmail.com
"""

#aqui conectamos con la base de datos, si no existe lo creamos
con = sqlite3.connect("tutorialtarea.db")
#creamos un cursor, es el canal de comunicacion
cur = con.cursor()

cur.execute("CREATE TABLE test(nombre, apellido, calificacion)")
""""""

data =[
    ("Saul", "Flores", 96),
    ("Maka", "Albarm", 56),
    ("Max", "Black", 86)
]

cur.executemany("INSERT INTO test VALUES ()", data)
con.commit()

