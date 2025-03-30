/*
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
*/


#include <iostream>     // Incluye la librería para entrada y salida estándar (cin, cout)
#include <set>          // Incluye la librería para poder usar conjuntos (set)
using namespace std;    // Nos permite usar cin, cout, set sin anteponer std::

int sumaCuadrados(int n);

int main() {

    int numero; // Declaramos la variable que almacenará el número introducido por el usuario

    // Mostramos un mensaje para indicar al usuario qué debe hacer
    cout << "Introduce un número positivo para comprobar si es feliz: ";

    // Leemos el número desde la entrada estándar
    cin >> numero;

    // Creamos un conjunto de enteros para almacenar los números intermedios y detectar repeticiones
    set<int> numerosVistos;


    while (numero != 1 && numerosVistos.find(numero) == numerosVistos.end())
    {

      numerosVistos.insert(numero);     // Guardamos el número actual
      numero = sumaCuadrados(numero);   // Calculamos el siguiente número
      
    }

    if (numero == 1){
      cout << "El número es feliz" << endl;
    }else { 
      cout << "El número no es feliz." << endl;
    }
    
    



}

// Función que calcula la suma de los cuadrados de los dígitos de un número
int sumaCuadrados(int n) {
  int suma = 0;  // Inicializamos la suma

  while (n > 0) {
      int digito = n % 10;        // Extraemos el último dígito
      suma += digito * digito;    // Elevamos al cuadrado y lo sumamos
      n = n / 10;                 // Eliminamos el último dígito
  }

  return suma;  // Devolvemos el resultado final
}
