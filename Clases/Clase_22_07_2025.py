#Librerias y Modulos
#Modulo es un archivo que contiene variables, funciones, clases y sentencias. 
#Tres tipos de modilos 
# 1.- Libreria estandar 
# 2.-Libreria o modulos propios, clases o archivos que nosotros creamos 
# 3- Librerias o modulos de terceros(las que no son ni de nosotros o vienen incluidas en la libreria estandaer)

#PIP: Ademas ser libreria nos permite gestionar paquetes y librerias




import sqlite3  # Importamos la librería para trabajar con SQLite
import os       # Para poder eliminar el archivo después

# Creamos o abrimos la base de datos
con = sqlite3.connect("tutorialtarea.db")
cur = con.cursor()

# Creamos una tabla llamada 'test' con tres columnas
cur.execute("CREATE TABLE test(nombre, apellido, calificacion)")

# Datos que vamos a insertar
data = [
    ("Juan", "Robles", 7.9),
    ("Pedro", "Picapiedra", 7.5),
    ("Javier", "Robles", 8.0),
]

# Insertamos todos los datos a la tabla
cur.executemany("INSERT INTO test VALUES(?, ?, ?)", data)

# Guardamos los cambios
con.commit()

# Consultamos todos los registros, ordenados por calificación
for row in cur.execute("SELECT nombre, apellido, calificacion FROM test ORDER BY calificacion"):
    print(row)  # Mostramos cada fila (tupla)

# Cerramos la conexión con la base de datos
con.close()

# Eliminamos el archivo .db después de usarlo
os.remove("tutorialtarea.db")