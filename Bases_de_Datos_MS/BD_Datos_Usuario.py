import mysql.connector  # Importamos el conector para MySQL

# Intentamos establecer la conexión con la base de datos
try:
    conexion = mysql.connector.connect(
        host="127.0.0.1",       # Dirección del servidor MySQL (localhost)
        user="root",            # Usuario de MySQL
        password="Blackapple1997",  # Contraseña del usuario MySQL
        database="clientes_db"  # Nombre de la base de datos a usar
    )
    print("✅ Conexión exitosa a la base de datos MySQL")
except mysql.connector.Error as err:
    print(f"❌ Error al conectar a MySQL: {err}")

# Creamos un cursor para ejecutar consultas SQL
cursor = conexion.cursor()

# Clase Cliente
class Cliente:
    def __init__(self, nombre, edad, telefono, correo, ciudad, marca_favorita):
        self.nombre = nombre
        self.edad = int(edad)
        self.telefono = telefono
        self.correo = correo
        self.ciudad = ciudad
        self.marca_favorita = marca_favorita
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Método de la clase Cliente para guardar un nuevo cliente en la base de datos
def registrar_en_bd(self):
    # Consulta SQL para insertar un nuevo registro en la tabla 'clientes'
    # Los valores %s actúan como marcadores de posición para evitar inyección SQL
    sql = """
    INSERT INTO clientes (nombre, edad, telefono, correo, ciudad, marca_favorita)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    # Creamos una tupla con los datos del cliente (provenientes de los atributos del objeto)
    valores = (
        self.nombre,         # Nombre del cliente
        self.edad,           # Edad del cliente
        self.telefono,       # Número de teléfono
        self.correo,         # Correo electrónico
        self.ciudad,         # Ciudad donde vive
        self.marca_favorita  # Marca preferida
    )

    try:
        # Ejecutamos la consulta SQL usando el cursor, pasando la consulta y los valores
        cursor.execute(sql, valores)

        # Guardamos (confirmamos) los cambios en la base de datos
        conexion.commit()

        # Mensaje de confirmación en consola
        print("✅ Cliente registrado correctamente.")

    except mysql.connector.Error as err:
        # Si ocurre un error en la inserción, lo mostramos en consola
        print(f"❌ Error al insertar en la base de datos: {err}")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Función para registrar cliente
def registrar_cliente():
    print("Ingrese los datos del nuevo cliente:")
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    telefono = input("Teléfono: ")
    correo = input("Correo electrónico: ")
    ciudad = input("Ciudad: ")
    marca_favorita = input("Marca favorita: ")

    nuevo_cliente = Cliente(nombre, edad, telefono, correo, ciudad, marca_favorita)
    nuevo_cliente.registrar_en_bd()
# Función para buscar clientes por nombre parcial
# Función para buscar clientes por nombre (puede ser parcial, no es necesario escribirlo completo)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def buscar_cliente_por_nombre():
    # Pedimos al usuario que ingrese el nombre o parte del nombre que desea buscar
    nombre_buscar = input("Ingrese el nombre o parte del nombre del cliente: ")

    # Definimos la consulta SQL usando LIKE para búsqueda parcial (los % permiten coincidencias parciales)
    sql = """
    SELECT id, nombre, edad, telefono, correo, ciudad, marca_favorita 
    FROM clientes 
    WHERE nombre LIKE %s
    """
    # Creamos la tupla con el valor a buscar, agregando % antes y después para que funcione el LIKE
    valores = (f"%{nombre_buscar}%",)
    
    try:
        # Ejecutamos la consulta SQL pasando los valores
        cursor.execute(sql, valores)

        # Obtenemos todos los resultados encontrados en forma de lista de tuplas
        resultados = cursor.fetchall()

        # Si hay resultados, los mostramos
        if resultados:
            print("\n📋 Resultados encontrados:")
            for cliente in resultados:
                # cliente[i] accede al campo correspondiente según el orden del SELECT
                print(
                    f"ID: {cliente[0]}, "
                    f"Nombre: {cliente[1]}, "
                    f"Edad: {cliente[2]}, "
                    f"Teléfono: {cliente[3]}, "
                    f"Correo: {cliente[4]}, "
                    f"Ciudad: {cliente[5]}, "
                    f"Marca Favorita: {cliente[6]}"
                )
        else:
            # Si no se encuentra nada, se muestra este mensaje
            print("❌ No se encontraron clientes con ese nombre.")

    except mysql.connector.Error as err:
        # Capturamos y mostramos cualquier error que ocurra en la consulta
        print(f"❌ Error en la búsqueda: {err}")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Menú principal
if __name__ == "__main__":
    while True:
        Entrada = input(
            "\n--- MENÚ ---\n"
            "1. Registrar Nuevo Cliente\n"
            "2. Consulta de clientes\n"
            "3. Salir\n"
            "Elige una opción: "
        )
        try:
            if Entrada == "1":
                registrar_cliente()
            elif Entrada == "2":
                buscar_cliente_por_nombre()
            elif Entrada == "3":
                print("👋 Finalizando Programa, buen día.")
                cursor.close()
                conexion.close()
                break
            else:
                print("⚠ Opción no válida, intenta con otra.")
        except ValueError:
            print("⚠ Error, opción no reconocida.")