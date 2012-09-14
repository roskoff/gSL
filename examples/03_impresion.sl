programa impresion
var
   texto: cadena
   n : numerico

inicio

   // Texto
   imprimir("Hola Mundo")

   // Texto y expresion aritmetica
   imprimir("5 - 2 = ", 5 - 2)

   // Varios textos
   imprimir("Fila 1", "Fila 2", "Fila 3")
   imprimir("------", "------", "------")
   imprimir("   100", "   200", "   300")
   imprimir("   101", "   202", "   303")
   imprimir("")


   // Impresion de variables
   texto = "Total Fila 3:"
   n = 300 + 303
   imprimir(texto, n)
fin
