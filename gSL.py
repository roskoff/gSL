import sys
from gSLParser import gSLParser

if __name__ == "__main__":
    # Interpretaremos el archivo pasado por linea de comandos
    file = open(sys.argv[1])
    source_code = file.read()

    # Creamos el parser
    gParser = gSLParser(debug = True)

    # Generamos el AST
    tree = gParser.parse(source_code, debug=0)

    # Compilamos y ejecutamos con el compilador de Python
    exec compile(tree, "<gsl_source_code>", "exec")


