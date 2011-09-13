import sys
if "../.." not in sys.path: sys.path.insert(0,"../..")
from gSLLexer import *
import ply.lex as lex

code = """var
a:numerico
"""
gLexer = gSLLexer()
lex.runmain(data = code)
