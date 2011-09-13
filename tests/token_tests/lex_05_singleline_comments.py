import sys
if "../.." not in sys.path: sys.path.insert(0,"../..")
from gSLLexer import *
import ply.lex as lex

code = """// Este es un comentario una linea
// Este comentario esta en otra linea
// Las tres lineas se deben ignorar por completo
"""
gLexer = gSLLexer()
lex.runmain(data = code)
