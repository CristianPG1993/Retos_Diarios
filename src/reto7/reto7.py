import random
import time

def main():
    pasos = int(input("¿Cuántos pasos quieres en la carrera?"))

    pasos_caracol_1 = 0
    pasos_caracol_2 = 0

    for i in range(pasos):
        velocidad_caracol_1 = random.randint(1, 5)
        velocidad_caracol_2 = random.randint(1, 5)

        pasos_caracol_1 += velocidad_caracol_1
        pasos_caracol_2 += velocidad_caracol_2

        print(f"Paso {i + 1}:")
        print(f"Pasos caracol 1: {velocidad_caracol_1}. Total: {pasos_caracol_1}")
        print(f"Pasos caracol 2: {velocidad_caracol_2}. Total: {pasos_caracol_2}")
        print("----------------------------------")

        time.sleep(0.5)  # Pausa de medio segundo

    # Comparamos las posiciones finales después del bucle
    if pasos_caracol_1 > pasos_caracol_2:
        print("El caracol 1 es el ganador!!")
    elif pasos_caracol_1 < pasos_caracol_2:
        print("El caracol 2 es el ganador!!")
    else:
        print("¡Empateee!")

# Llamamos a la función main
main()
