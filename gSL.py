# -*- coding: utf-8 -*-
import sys
import argparse
from gSLParser import gSLParser

# Esta función retorna todas las funciones predeterminadas en SL, el
# conjunto de todas ellas sería nuestro RunTime Library (RTL)
def getRTL():
    from ast import FunctionDef, For, Name
    from ast import Load, Store, arguments, Expr, Call, Str, keyword
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
                                                 varargannotation = None,
                                                 kwonlyargs = [],
                                                 kwarg = None,
                                                 kwargannotation = None,
                                                 defaults = [],
                                                 kw_defaults = []),
                                body = [For(target = Name(id = 'arg', ctx=Store()),
                                            iter   = Name(id = 'args', ctx=Load()),
                                            body   = [Expr(value = Call(func = Name(id = 'print', ctx = Load()),
                                                                        args = [Name(id = 'arg', ctx = Load())],
                                                                        keywords = [keyword(arg = 'end', value = Str(s = ' '))],
                                                                        stararg = None,
                                                                        kwargs = None))],
                                            orelse = []),
                                        Expr(value = Call(func = Name(id = 'print', ctx = Load()),
                                                                        args = [],
                                                                        keywords = [],
                                                                        stararg = None,
                                                                        kwargs = None))],
                                        decorator_list = [],
                                        returns = None))
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
        print(formatTree(ast.dump(tree, True, False)))

    # Agregar funciones predeterminadas
    tree.body = getRTL() + tree.body
    tree = ast.fix_missing_locations(tree)

    # Compilamos y ejecutamos con el compilador de Python
    exec(compile(tree, "<gsl_source_code>", "exec"))


