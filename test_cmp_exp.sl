var
  a : cadena
  b : cadena
inicio
   si (2 == 1){
      imprimir ("Hola Mundo!")
   sino
      imprimir ("Adios!")
   }

   si (12 < 11){
      imprimir ("Esto no se imprime")
   sino
      imprimir (";)")
   }

   si (0 <= 1){ imprimir("1 <= 1") } 
   si (0 >= 1){ imprimir("1 >= 1") }
   si (0 == 1){ imprimir("1 == 1") }
   si (1 <> 1){ imprimir("0 <> 1") }

   a = "a"
   b = "b"
   si (a < b) { imprimir(" a < b ") }

   b = a
fin
