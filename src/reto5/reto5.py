from turtledemo.paint import switchupdown  # Jordi nunca se acuerda de abrir las exclamaciones.
 #  Él dice que es porque en catalán no se abren las exclamaciones,
 #  pero yo creo que simplemente no sabe escribir.
 #  Vamos a crear un programa que asegure que hay tantos abrir exclamación (¡)
 #  como cerrar exclamación (!) para flamearlo.
 #
 #    Ejemplo
 #    Entrada = ¡¡¡Caramba!!! ¡Hola!
 #    Salida = Si No


frase = input("Introduce una frase: ")

contador_abiertas = 0
contador_cerradas = 0

# Bucle indentado correctamente
for letra in frase:
    if letra == '¡':
        contador_abiertas += 1
    elif letra == '!':
        contador_cerradas += 1

# Comparación de los contadores
if contador_abiertas == contador_cerradas:
    print("Tienes que ser Góngora!! ")
else:
    print("Vete a estudiar!!")
