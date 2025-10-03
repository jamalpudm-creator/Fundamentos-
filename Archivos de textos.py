
# Abrir el archivo en modo escritura ('w')
archivo = open('my_notes.txt', 'w')

#Líneas de notas personales utilizando write()
archivo.write("Nota 1: Madrugar todos los días  que tengas más tiempo para hacer las cosas .\n")
archivo.write("Nota 2: Preparar todos los deberes de la Unversidad hasta el domingo.\n")
archivo.write("Nota 3: Tener en cuenta que toca estudair para los examenes esta semana.\n")

# Cerrar el archivo después de la escritura para guardar los cambios
archivo.close()

print("Archivo my_notes.txt creado y escrito exitosamente.")

# Lectura de Archivo de Texto
# Abrir el archivo en modo lectura ('r')
archivo = open('my_notes.txt', 'r')

# Leer el contenido línea por línea utilizando readline()
linea = archivo.readline()

# Mostrar cada línea leída en la consola utilizando un bucle while
while linea != '':
    print(linea.strip())  # strip() elimina el salto de línea
    linea = archivo.readline()

# Cerrar el archivo después de la lectura
archivo.close()
