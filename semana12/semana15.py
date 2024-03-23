# Diccionario informacion_personal
informacion_personal = {
    "nombre": "KarenAG",
    "edad": 23,
    "ciudad": "Ciudad Tena",
    "profesion": "Estudiante de Ingeniería"
}

# Acceder a la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Ciudad Riobaba"

# Agregar una nueva clave-valor que represente a la "profesion"
informacion_personal["profesion"] = "Ingeniera en Sistemas"

# Verificar si la clave "telefono" existe y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "062858114"

# Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario resultante
print(informacion_personal)
