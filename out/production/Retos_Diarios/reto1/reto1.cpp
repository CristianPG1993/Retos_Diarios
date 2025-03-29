/*
Ejercicio 1: Dados los números del 1 hasta un número positivo introducido por el usuario, calcular:
 - La suma total de los números pares.
 - Cuántos números impares hay en total.
*/
#include <iostream>
using namespace std;


int main(){

    //Iniciamos la variable
    int numero; 

    //Pedimos al usuario el número
    cout << "Introduce un número positivo: ";
    cin >> numero;


    //Iniciamos las otras variables para almacenar la suma de los pares y la cantidad de números impares

    int suma_pares = 0;
    int contador_impares = 0;


    for (int i = 1; i <= numero; i++){
        if(i % 2 == 0){
            suma_pares += i;
        }else {
            contador_impares ++;

        }
    }

    cout << "La suma de los números desde el 1 hasta el " << numero << " es: " << suma_pares << endl;
    cout << "La cantidad de números impares desde el 1 hasta el " << numero << " es: " << contador_impares << endl;


}

