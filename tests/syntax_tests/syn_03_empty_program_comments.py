import sys
from ast import *
if "../.." not in sys.path: sys.path.insert(0,"../..")
from gSLParser import gSLParser

source_code = """programa nombre_programa
inicio
// Aqui hay un comentario de una linea

/* Aqui hay otro comentario
que ocupa mas de una
linea
*/

fin
"""

gParser = gSLParser(debug = False)
tree = gParser.parse(source_code, debug = 0)
print dump(tree)

#exec compile(tree, "<gsl_source_code>", "exec")


