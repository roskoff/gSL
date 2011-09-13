import sys
if "../.." not in sys.path: sys.path.insert(0,"../..")
from gSLLexer import *
import ply.lex as lex

code = """0
1.0
5.25
1024e2
1024E2
1024e+2
1024E+2
512e5
512E5
10000e-2
10000E-2
3.14e2
3.14E2
25.00e-2
25.00E-2
"""
gLexer = gSLLexer()
lex.runmain(data = code)
