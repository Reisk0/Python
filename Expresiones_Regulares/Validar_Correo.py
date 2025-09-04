import re  # Importamos el módulo de expresiones regulares

# Expresión regular para validar correos electrónicos simples
patron_correo = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'

# Función para validar correo
def es_correo_valido(correo):
    # Utilizamos re.match para comparar el patrón desde el inicio
    if re.match(patron_correo, correo):
        return True
    else:
        return False

# Ejemplos de prueba
correos = [
    "usuario@email.com",
    "nombre.apellido@dominio.mx",
    "correo_invalido@",
    "sin-arroba.com",
    "otro@ejemplo.org"
]

# Probar la función
for c in correos:
    if es_correo_valido(c):
        print(f"✅ '{c}' es válido")
    else:
        print(f"❌ '{c}' es inválido")