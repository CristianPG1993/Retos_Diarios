"""
Ejercicio 3: Número Feliz

Un número se llama feliz si, al reemplazarlo repetidamente por la suma
de los cuadrados de sus dígitos, eventualmente llega al número 1.
Si entra en un bucle que nunca alcanza el 1, se considera infeliz.

Ejemplo:
- El número 19 es feliz:
  1² + 9² = 82
  8² + 2² = 68
  6² + 8² = 100
  1² + 0² + 0² = 1

Objetivo:
Pedir al usuario un número y determinar si es un número feliz o no.
"""

# Preguntar al usuario por un número y almacenarlo en una variable.
numero = int(input("Introduce un número para comprobar si es feliz: "))

# Creamos un set() para almacenar los números intermedios
# que se generan durante el proceso. Esto nos ayuda a detectar ciclos.
numeros_vistos = set()

# Función para coger un número, extraer sus dígitos,
# elevar cada dígito al cuadrado y devolver la suma.
def suma_cuadrado(n):
    suma = 0                    # Declaramos la variable dentro de la función
    while n > 0:
        digito = n % 10         # Extraemos el último dígito del número
        suma += digito * digito # Elevamos al cuadrado el dígito y lo acumulamos
        n = n // 10             # Eliminamos el último dígito del número
    return suma                 # Devolvemos la suma total

# Bucle principal: se repite mientras no lleguemos a 1 y el número no se haya repetido
while numero != 1 and numero not in numeros_vistos:
    numeros_vistos.add(numero)         # Guardamos el número actual para detectar ciclos
    numero = suma_cuadrado(numero)     # Calculamos la suma de cuadrados de sus dígitos

# Resultado final después del bucle:
# Si llegamos a 1, el número es feliz. Si se repitió, no lo es.
if numero == 1:
    print("¡El número es feliz! 😄")
else:
    print("El número NO es feliz. 😢")
