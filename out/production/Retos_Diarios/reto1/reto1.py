"""
Ejercicio 1: Dados los números del 1 hasta un número positivo introducido por el usuario, calcular:
 - La suma total de los números pares.
 - Cuántos números impares hay en total.
"""

numero = int(input("Introduce un número positivo: "))


suma_pares = 0
numeros_impares = 0

for i in range(1, numero + 1):
    if i % 2 == 0:
        suma_pares +=i
    else:
        numeros_impares +=1

print(f"La suma de los números del 1 hasta el {numero} es: {suma_pares}")
print(f"La cantida de números impares desde el 1 hasta el {numero} es: {numeros_impares}")
