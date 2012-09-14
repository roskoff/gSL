# -*- coding: utf-8 -*-
import sys
import argparse
from gSLParser import gSLParser

# Esta función retorna todas las funciones predeterminadas en SL, el
# conjunto de todas ellas sería nuestro RunTime Library (RTL)
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
    arg_parser = argparse.ArgumentParser(description = 'gSL - Intérprete para el lenguaje SL')
    arg_parser.add_argument('-d', '--print-debug', action='store_true')
    arg_parser.add_argument('-t', '--print-ast', action='store_true')
    arg_parser.add_argument('archivo_fuente')
    argumentos = arg_parser.parse_args()

    # Interpretaremos el archivo pasado por linea de comandos
    file = open(argumentos.archivo_fuente)
    source_code = file.read()

    # Creamos el parser
    gParser = gSLParser(debug = argumentos.print_debug)

    # Generamos el AST
    tree = gParser.parse(source_code, debug=0)

    import ast
    # Imprimir opcionalmente el AST (sin el RTL)
    if argumentos.print_ast:
        from util import formatTree
        print formatTree(ast.dump(tree, True, False))

    # Agregar funciones predeterminadas
    tree.body = getRTL() + tree.body
    tree = ast.fix_missing_locations(tree)

    # Compilamos y ejecutamos con el compilador de Python
    exec compile(tree, "<gsl_source_code>", "exec")


