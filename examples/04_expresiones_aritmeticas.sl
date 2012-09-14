programa expresiones_aritmeticas
var
  a : numerico
  b : numerico
  c : numerico

inicio

   a = 15
   b = 2
   c = a * b

   imprimir("a:", a)
   imprimir("b:", b)
   imprimir("c:", c)

   a = a * c / b - 25 * a + c / 1 * b + (13 - c)
   // a * c = 450
   // a = 450 / b - 25 * a + c / 1 * b + (13 - c)
   // 450 / b = 225
   // a = 225 - 25 * a + c / 1 * b + (13 - c)
   // 25 * a = 375
   // a = 225 - 375 + c / 1 * b + (13 - c)
   // c / 1 = 30
   // a = 225 - 375 + 30 * b + (13 - c)
   // 30 * b = 60
   // a = 225 - 375 + 60 + (13 - c)
   // 13 - c = -17
   // a = 225 - 375 + 60 + (-17)
   // a = 225 - 375 + 60 - 17
   // 225 - 375 = - 150
   // a = - 150 + 60 - 17
   // - 150 + 60 = -90
   // a = - 90 - 17 
   // a = - 107

   imprimir("a:", a)

fin
