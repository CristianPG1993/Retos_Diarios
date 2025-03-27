package reto2;

import java.util.Scanner; // Importamos la clase Scanner para leer datos del usuario

import java.util.HashSet; // Importamos la clase HashSet para detectar repeticiones
                          // y evitar bulces infinitos

public class reto2 {

    public static void main(String[] args) {
        /*
          Ejercicio 3: Número Feliz

          Un número se llama feliz si, al reemplazarlo repetidamente por la suma
          de los cuadrados de sus dígitos,
          eventualmente llega al número 1. Si entra en un bucle que nunca alcanza
          el 1, se considera un número infeliz.

          Ejemplo:
          - El número 19 es feliz:
          1² + 9² = 82
          8² + 2² = 68
          6² + 8² = 100
          1² + 0² + 0² = 1

          Objetivo:
          Pedir al usuario un número y determinar si es un número feliz o no.

         */

        // Generamos la petición de la variable al usuario

        Scanner scanner = new Scanner(System.in);
        System.out.println("Bienvenido, ¡Comprueba si el número es feliz!");
        System.out.println("Introduce un número: ");
        int numero = scanner.nextInt();

        // Creamos la variable numerosVistos para guardar cada número intermedio
        HashSet<Integer> numerosVistos = new HashSet<>();

        //Ponemos un bucle do - while para comprobar si el número es feliz que mientras el número
        // sea diferente de 1 o no lo hayamos visto antes en el bucle.

        do {
            numerosVistos.add(numero);             // Guarda el número actual para detectar bucles
            numero = sumaCuadrados(numero);        // Calcula el nuevo número transformado
        } while (numero != 1 && !numerosVistos.contains(numero));

        if (numero == 1) {
            System.out.println("¡El número es feliz! 😄");
        } else {
            System.out.println("El número NO es feliz. 😢");
        }


    }

    // Función que calcula la suma de los cuadrados de los dígitos de un número
    public static int sumaCuadrados(int n) {

        int suma = 0; // Variable acumuladora para la suma de cuadrados

        // Mientras el número tenga dígitos
        while (n > 0) {
            int digito = n % 10;           // Extraemos el último dígito
            suma += digito * digito;       // Elevamos al cuadrado y lo sumamos
            n = n / 10;                    // Eliminamos el último dígito
        }

        return suma; // Devolvemos la suma total
    }


}
