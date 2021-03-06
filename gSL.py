import sys
from gSLParser import gSLParser

def getRTL():
    from ast import FunctionDef, For, Print, Name, Load, Store, arguments
    functions = []

    # imprimir(...)
    # Recibe cero o mas expresiones separadas por coma y las
    # imprme en pantalla separadas por un espacio
    #
    # Codigo Python
    # def imprimir(*args):
    #     for arg in args:
    #         print arg,
    #     print
    #
    functions.append(FunctionDef(name = 'imprimir', 
                                args = arguments(args   = [],
                                                 vararg = 'args', 
                                                 kwarg  = None,
                                                 defaults = []),
                                body = [For(target = Name(id = 'arg', ctx=Store()), 
                                            iter   = Name(id = 'args', ctx=Load()), 
                                            body   = [Print(dest = None, values = [Name(id = 'arg', ctx=Load())], nl=False)],
                                            orelse=[]), 
                                        Print(dest=None, values=[], nl=True)], 
                                decorator_list=[]))
    return functions

if __name__ == "__main__":
    # Interpretaremos el archivo pasado por linea de comandos
    file = open(sys.argv[1])
    source_code = file.read()

    # Creamos el parser
    gParser = gSLParser(debug = True)

    # Generamos el AST
    tree = gParser.parse(source_code, debug=0)

    # Agregar funciones predeterminadas
    tree.body = getRTL() + tree.body
    import ast
    tree = ast.fix_missing_locations(tree)
    #print ast.dump(tree, True, True)

    # Compilamos y ejecutamos con el compilador de Python
    exec compile(tree, "<gsl_source_code>", "exec")


