# Pedir al usuario que ingrese el nombre del archivo que desea procesar
nombre_archivo = input("Ingrese el nombre del archivo que desea procesar: ")

# Abrir el archivo de correo
with open(nombre_archivo) as archivo:
    # Crear un diccionario vacío para contar los correos recibidos de cada dominio
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
                dominio = direccion.split("@")[-1]
                conteos[dominio] = conteos.get(dominio, 0) + 1

# Imprimir el histograma de dominios de correo electrónico
for dominio, conteo in conteos.items():
    print(dominio, conteo)
