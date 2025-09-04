#COMO CONECTAR PYTHON CON MYSQL WORKBRACH.

import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Blackapple1997"
    )
    print("✅ Conexión exitosa a la base de datos MySQL")
except mysql.connector.Error as err:
    print(f"❌ Error al conectar a MySQL: {err}")



        