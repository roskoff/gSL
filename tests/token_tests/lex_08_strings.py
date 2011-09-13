# -*- coding: utf-8 -*-
import sys
if "../.." not in sys.path: sys.path.insert(0,"../..")
from gSLLexer import *
import ply.lex as lex

code = """"texto literal"
'comillas simples'
"La dama exclamó: 'Oh! Déjenlo ir!'"
'esta es una "cita"'
"""
gLexer = gSLLexer()
lex.runmain(data = code)
