# Pedir al usuario que ingrese el nombre del archivo que desea procesar
nombre_archivo = input("Ingrese el nombre del archivo que desea procesar: ")

# Abrir el archivo de correo
with open(nombre_archivo) as archivo:
    # Crear un diccionario vacío para contar los correos recibidos en cada día de la semana
    conteos = {}

    # Utilizar un bucle para procesar cada línea del archivo
    for linea in archivo:
        # Si la línea comienza con "From", procesarla
        if linea.startswith("From"):
            # Dividir la línea en palabras
            palabras = linea.split()

            # Si la línea tiene al menos tres palabras (y la tercera es el día de la semana), contar el correo
            if len(palabras) >= 3 and palabras[2] in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]:
                dia_semana = palabras[2]
                conteos[dia_semana] = conteos.get(dia_semana, 0) + 1

# Imprimir los conteos de correos recibidos en cada día de la semana
for dia_semana in conteos:
    print(dia_semana, conteos[dia_semana])
