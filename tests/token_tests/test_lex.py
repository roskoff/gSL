import unittest
try:
    import io
except ImportError:
    import io as StringIO

import sys
if "../.." not in sys.path: sys.path.insert(0,"../..")
from gSLLexer import gSLLexer
import ply.lex as lex

def check_expected(result,expected):
    if sys.version_info[0] >= 3:
        if isinstance(result,str):
            result = result.encode('ascii')
        if isinstance(expected,str):
            expected = expected.encode('ascii')
    resultlines = result.splitlines()
    expectedlines = expected.splitlines()

    if len(resultlines) != len(expectedlines):
        return False

    for rline,eline in zip(resultlines,expectedlines):
        if not rline.endswith(eline):
            return False
    return True

def run_import(module):
    code = "import "+module
    exec(code)
    del sys.modules[module]

class TestLexReservedWords(unittest.TestCase):
    def setUp(self):
        sys.stderr = io.StringIO()
        sys.stdout = io.StringIO()
    def tearDown(self):
        sys.stderr = sys.__stderr__
        sys.stdout = sys.__stdout__

    def test_lex_01_reserved_words(self):
        gLexer = gSLLexer()
        #lex.runmain(data = "and archivo caso const constantes desde eval fin\n"
                           #"hasta inicio lib libext matriz mientras not or\n" 
                           #"paso programa ref registro repetir retorna si\n"
                           #"sino sub subrutina tipos var variables vector\n")
        run_import("lex_01_reserved_words")
        result = sys.stdout.getvalue()
        self.assert_(check_expected(result,
        #self.assertEquals(result,
                                    "(AND,'and',1,0)\n"
                                    "(ARCHIVO,'archivo',1,4)\n"
                                    "(CASO,'caso',1,12)\n"
                                    "(CONSTANTES,'const',1,17)\n"
                                    "(CONSTANTES,'constantes',1,23)\n"
                                    "(DESDE,'desde',1,34)\n"
                                    "(EVAL,'eval',1,40)\n"
                                    "(FIN,'fin',1,45)\n"
                                    "(HASTA,'hasta',2,49)\n"
                                    "(INICIO,'inicio',2,55)\n"
                                    "(LIB,'lib',2,62)\n"
                                    "(LIBEXT,'libext',2,66)\n"
                                    "(MATRIZ,'matriz',2,73)\n"
                                    "(MIENTRAS,'mientras',2,80)\n"
                                    "(NOT,'not',2,89)\n"
                                    "(OR,'or',2,93)\n"
                                    "(PASO,'paso',3,96)\n"
                                    "(PROGRAMA,'programa',3,101)\n"
                                    "(REF,'ref',3,110)\n"
                                    "(REGISTRO,'registro',3,114)\n"
                                    "(REPETIR,'repetir',3,123)\n"
                                    "(RETORNA,'retorna',3,131)\n"
                                    "(SI,'si',3,139)\n"
                                    "(SINO,'sino',4,142)\n"
                                    "(SUBRUTINA,'sub',4,147)\n"
                                    "(SUBRUTINA,'subrutina',4,151)\n"
                                    "(TIPOS,'tipos',4,161)\n"
                                    "(VARIABLES,'var',4,167)\n"
				    "(VARIABLES,'variables',4,171)\n"
				    "(VECTOR,'vector',4,181)\n")
                     )

    def test_lex_02_var_declaration(self):
        run_import("lex_02_var_declaration")
        result = sys.stdout.getvalue()
        self.assert_(check_expected(result,
        #self.assertEquals(result,
                                    "(VARIABLES,'var',1,0)\n"
                                    "(IDENTIFICADOR,'a',2,4)\n"
                                    "(DOS_PUNTOS,':',2,5)\n"
                                    "(IDENTIFICADOR,'numerico',2,6)\n")
                    )
    
    def test_lex_03_symbols(self):
        run_import("lex_03_symbols")
        result = sys.stdout.getvalue()
        self.assert_(check_expected(result,
        #self.assertEquals(result,
                                    "(S_MAS,'+',1,0)\n"
                                    "(S_MENOS,'-',1,1)\n"
                                    "(S_MULT,'*',1,2)\n"
                                    "(S_DIV,'/',1,3)\n"
                                    "(S_ASIGNACION,'=',1,4)\n"
                                    "(PAREN_I,'(',1,5)\n"
                                    "(PAREN_D,')',1,6)\n"
                                    "(LLAVE_I,'{',1,7)\n"
                                    "(LLAVE_D,'}',1,8)\n"
                                    "(CORCH_I,'[',1,9)\n"
                                    "(CORCH_D,']',1,10)\n"
                                    "(PUNTO,'.',1,11)\n"
                                    "(COMA,',',1,12)\n"
                                    "(PUNTO_Y_COMA,';',1,13)\n"
                                    "(DOS_PUNTOS,':',1,14)\n"
                                    "(COMILLA_SIMPLE,\"'\",1,15)\n"
                                    "(COMILLA_DOBLE,'\"',1,16)\n")
                    )
    
    def test_lex_04_multiline_commments(self):
        run_import("lex_04_multiline_comments")
        result = sys.stdout.getvalue()
        self.assert_(check_expected(result, ""))
        #self.assertEquals(result, "")
    
    def test_lex_05_singleline_commments(self):
        run_import("lex_05_singleline_comments")
        result = sys.stdout.getvalue()
        self.assert_(check_expected(result, ""))
        #self.assertEquals(result, "")

    def test_lex_06_numbers(self):
        run_import("lex_06_numbers")
        result = sys.stdout.getvalue()
        self.assert_(check_expected(result, 
        #self.assertEquals(result, 
                                    "(NUMERO,0.0,1,0)\n"
                                    "(NUMERO,1.0,2,2)\n"
                                    "(NUMERO,5.25,3,6)\n"
                                    "(NUMERO,102400.0,4,11)\n"
                                    "(NUMERO,102400.0,5,18)\n"
                                    "(NUMERO,102400.0,6,25)\n"
                                    "(NUMERO,102400.0,7,33)\n"
                                    "(NUMERO,51200000.0,8,41)\n"
                                    "(NUMERO,51200000.0,9,47)\n"
                                    "(NUMERO,100.0,10,53)\n"
                                    "(NUMERO,100.0,11,62)\n"
                                    "(NUMERO,314.0,12,71)\n"
                                    "(NUMERO,314.0,13,78)\n"
                                    "(NUMERO,0.25,14,85)\n"
                                    "(NUMERO,0.25,15,94)\n")
                    )
    
    def test_lex_07_id(self):
        run_import("lex_07_id")
        result = sys.stdout.getvalue()
        self.assert_(check_expected(result, 
        #self.assertEquals(result, 
                                    "(IDENTIFICADOR,'variable',1,0)\n"
                                    "(IDENTIFICADOR,'hasta_desde',2,9)\n"
                                    "(IDENTIFICADOR,'code',3,21)\n"
                                    "(IDENTIFICADOR,'numerico',4,26)\n"
                                    "(IDENTIFICADOR,'FALSE',5,35)\n"
                                    "(IDENTIFICADOR,'NO',6,41)\n"
                                    "(IDENTIFICADOR,'imprimir',7,44)\n"
                                    "(IDENTIFICADOR,'PROGRAMA',8,53)\n"
                                    "(IDENTIFICADOR,'unnombreconmaxtreintaydosletras',9,62)\n"
                                    "(IDENTIFICADOR,'unnombreconmaxtreintaydosletras',10,94)\n"
                                    "(IDENTIFICADOR,'_underscore',11,140)\n"
                                    "(IDENTIFICADOR,'\\xc3\\xb1emby',12,152)\n"
                                    "(IDENTIFICADOR,'\\xc3\\x91emby',13,159)\n"
                                    "(IDENTIFICADOR,'letra_e\\xc3\\xb1e',14,166)\n"
                                    "(IDENTIFICADOR,'A\\xc3\\x91O',15,177)\n"
                                    "(IDENTIFICADOR,'i',16,182)\n")
                    )

    def test_lex_08_strings(self):
        run_import("lex_08_strings")
        result = sys.stdout.getvalue()
        self.assert_(check_expected(result,
        #self.assertEquals(result, 
                                    "(CADENA,'\"texto literal\"',1,0)\n"
                                    "(CADENA,\"'comillas simples'\",2,16)\n"
                                    "(CADENA,'\"La dama exclam\\xc3\\xb3: \\\'Oh! D\\xc3\\xa9jenlo ir!\\\'\"',3,35)\n"
                                    "(CADENA,'\\\'esta es una \"cita\"\\\'',4,74)\n")
                    )

    def test_lex_09_ilegal_chars(self):
        run_import("lex_09_ilegal_chars")
        result = sys.stdout.getvalue()
        self.assert_(check_expected(result,
        #self.assertEquals(result,
                                    "Caracter ilegal: '#'\n"
                                    "Caracter ilegal: '@'\n"
                                    "Caracter ilegal: '\\'\n"
                                    "Caracter ilegal: '?'\n"
                                    "Caracter ilegal: '$'\n"
                                    "Caracter ilegal: '~'\n")
                    )

if __name__ == '__main__':
    unittest.main()
