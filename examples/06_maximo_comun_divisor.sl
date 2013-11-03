/*
 * Cálculo del máximo común divisor utilizando el algoritmo
 * de Euclides.
 *
 * (c) jsegovia@cnc.una.py
 */
var
   a : numerico 
   b : numerico
inicio
   // Usar dos enteros positivos
   a = 45
   b = 30
   mientras (a <> b ) {
      si ( a > b ) {
         a = a - b
      sino
         b = b - a
      }
   }
   imprimir ("El MCD es ", a)
fin
