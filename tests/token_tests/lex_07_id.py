# -*- coding: utf-8 -*-
import sys
if "../.." not in sys.path: sys.path.insert(0,"../..")
from gSLLexer import *
import ply.lex as lex

code = """variable
hasta_desde
code
numerico
FALSE
NO
imprimir
PROGRAMA
unnombreconmaxtreintaydosletras
unnombreconmaxtreintaydosletrasmasunascuantas
_underscore
ñemby
Ñemby
letra_eñe
AÑO
i
"""
gLexer = gSLLexer()
lex.runmain(data = code)
