#!/usr/bin/python2
# -*- coding: utf-8 -*-
import sys
import argparse
import runTimeLibrary
from gSLParser import gSLParser


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
        print "-------------- Inicio impresión de AST --------------"
        print formatTree(ast.dump(ast.fix_missing_locations(tree), True, True))
        print "-------------- Fin impresión de AST --------------"

    # Agregar funciones predeterminadas
    tree.body = runTimeLibrary.getFunctions() + tree.body
    tree = ast.fix_missing_locations(tree)

    # Compilamos y ejecutamos con el compilador de Python
    exec compile(tree, "<gsl_source_code>", "exec")


