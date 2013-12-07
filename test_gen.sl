var 
    k : numerico
    p : numerico
inicio
    // TODO Inicializar k
    k = 189993818138.0e+30
    eval {
        caso (1 > 1)
           imprimir("uno")
        caso (2 > 2)
           imprimir("dos")
        caso (3 > 8)
           imprimir("tres")
           imprimir("chau")
        caso (4 > 4)
           imprimir("cuatro")
        sino
            /* Agrupar varias instrucciones dentro de sino
             * a fin de probar su funcionamiento
             */
           imprimir("sino")
           imprimir("y que")
            si (21 > 3) {
              imprimir("a dormir")
            }
    }
fin
