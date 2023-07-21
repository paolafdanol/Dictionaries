# Pedir al usuario que ingrese el nombre del archivo que desea procesar
nombre_archivo = input("Ingrese el nombre del archivo que desea procesar: ")

# Abrir el archivo de correo
with open(nombre_archivo) as archivo:
    # Crear un diccionario vacío para contar los correos recibidos de cada dirección de correo electrónico
    conteos = {}

    # Utilizar un bucle para procesar cada línea del archivo
    for linea in archivo:
        # Si la línea comienza con "From", procesarla
        if linea.startswith("From"):
            # Dividir la línea en palabras
            palabras = linea.split()

            # Si la línea tiene al menos dos palabras (y la segunda es una dirección de correo electrónico), contar el correo
            if len(palabras) >= 2:
                direccion = palabras[1]
                conteos[direccion] = conteos.get(direccion, 0) + 1

# Imprimir el histograma de direcciones de correo electrónico
for direccion, conteo in conteos.items():
    print(direccion, conteo)

# Determinar quién tiene la mayoría de mensajes en el archivo
maximo_conteo = None
maximo_direccion = None
for direccion, conteo in conteos.items():
    if maximo_conteo is None or conteo > maximo_conteo:
        maximo_conteo = conteo
        maximo_direccion = direccion

# Imprimir quién tiene la mayoría de mensajes en el archivo
print("\nLa dirección de correo electrónico con la mayoría de mensajes es:", maximo_direccion)
print("Número de mensajes:", maximo_conteo)
