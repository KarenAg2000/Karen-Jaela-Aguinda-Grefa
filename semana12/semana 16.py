# Whiteboard

# Crear un nuevo archivo llamado my_notes.txt.
with open('my_notes.txt', 'w') as file:
    file.write("Linea 1: Comprar leche en la tienda.\n")
    file.write("Linea 2: Llamar a Viviana para organizar la fiesta.\n")
    file.write("Linea 3: Hacer ejercicio por la tarde.\n")

# Abrir el archivo en modo lectura
with open('my_notes.txt', 'r') as file:
    # Leer el contenido del archivo línea por línea utilizando readline()
    line = file.readline()
    # Mientras haya líneas por leer
    while line:
        # Mostrar cada línea leída en la consola
        print(line.strip())
        # Leer la siguiente línea
        line = file.readline()

# El archivo se cierra automáticamente al salir del bloque 'with'
