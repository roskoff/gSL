import sys
if "../.." not in sys.path: sys.path.insert(0,"../..")
from gSLLexer import *
import ply.lex as lex

code = """/* Este es un comentario multilinea
que deberia ignorarse
por completo */
"""
gLexer = gSLLexer()
lex.runmain(data = code)
