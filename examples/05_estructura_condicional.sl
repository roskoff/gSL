programa estructura_condicional
var
   n : numerico
inicio

   n = 5
   si (n == 25) {
      imprimir("n cuadrado")  // No imprime
   }

   n = n * n
   si (n > 30) {
      imprimir("n es mayor a 30")  // No imprime
   sino
      imprimir("n (", n, ") es menor a 30") // Si imprime
   }

   n = n / 2  // n ahora es 12.5

   // 12.5 - 5 es mayor a 3, pero 14 no es menor que 12.5,
   // por lo tanto la condicion es falsa
   si (n - 5 > 3 and 7 * 2 < n) { 
      imprimir("TRUE")
   sino
      imprimir("FALSE")
   }

fin
