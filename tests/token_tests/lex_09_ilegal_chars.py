# -*- coding: utf-8 -*-
import sys
if "../.." not in sys.path: sys.path.insert(0,"../..")
from gSLLexer import *
import ply.lex as lex

code = r"#@\?$~"
gLexer = gSLLexer()
lex.runmain(data = code)
