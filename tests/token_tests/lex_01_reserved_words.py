import sys
if "../.." not in sys.path: sys.path.insert(0,"../..")
from gSLLexer import *
import ply.lex as lex

code = """and archivo caso const constantes desde eval fin
hasta inicio lib libext matriz mientras not or
paso programa ref registro repetir retorna si
sino sub subrutina tipos var variables vector
"""
gLexer = gSLLexer()
lex.runmain(data = code)
