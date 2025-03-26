package reto1;

import java.util.Scanner;

public class reto1 {
    public static void main(String[] args) {

        // Pedir al usuario un número positivo
        Scanner scanner = new Scanner(System.in);
        System.out.println("Introduce un número positivo: ");
        int numeroPositivo = scanner.nextInt();

        // Inicializar variables para sumar números pares e impares
        int sumaPares = 0;
        int sumaImpares = 0;

        // Bucle para sumar números pares e impares
        for(int i = 1; i <= numeroPositivo; i++){
            if(i % 2 == 0){
                sumaPares += i;          // suma número par
            } else {
                sumaImpares ++;        // suma número impar
            }
        }

        // Mostrar resultados
        System.out.println("La suma de los números pares desde el 1 hasta el "
                + numeroPositivo + " es: " + sumaPares);
        System.out.println("La cantidad de números impares desde el 1 hasta el "
                + numeroPositivo + " es: " + sumaImpares);

        scanner.close();
    }
}