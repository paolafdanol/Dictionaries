# Abrir el archivo words.txt
with open("words.txt") as archivo:
    # Leer todas las palabras del archivo y almacenarlas en una lista
    palabras = archivo.read().split()

# Crear un diccionario vacío
diccionario = {}

# Utilizar un bucle para agregar cada palabra como clave al diccionario
for palabra in palabras:
    diccionario[palabra] = None

# Pedir al usuario que ingrese la palabra que desea buscar
palabra_buscada = input("Ingrese la palabra que desea buscar en el diccionario: ")

# Utilizar el operador in para revisar si la palabra buscada está en el diccionario
if palabra_buscada in diccionario:
    print("La palabra está en el diccionario.")
else:
    print("La palabra no está en el diccionario.")
