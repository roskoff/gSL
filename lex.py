#------------------------------------------------------------
# lex.py
#
# Tokenizer para las gSL
# ------------------------------------------------------------

import ply.lex as lex

# Palabras reservadas
reserved = {
    'and' : 'AND',
    'archivo' : 'ARCHIVO',
    'caso' : 'CASO',
    'const' : 'CONSTANTES',
    'constantes' : 'CONSTANTES',
    'desde' : 'DESDE',
    'eval' : 'EVAL',
    'fin' : 'FIN',
    'hasta' : 'HASTA',
    'inicio' : 'INICIO',
    'lib' : 'LIB',
    'libext' : 'LIBEXT',
    'matriz' : 'MATRIZ',
    'mientras' : 'MIENTRAS',
    'not' : 'NOT',
    'or' : 'OR',
    'paso' : 'PASO',
    'subrutina' : 'SUBRUTINA',
    'programa' : 'PROGRAMA',
    'ref' : 'REF',
    'registro' : 'REGISTRO',
    'repetir' : 'REPETIR',
    'retorna' : 'RETORNA',
    'si' : 'SI',
    'sino' : 'SINO',
    'tipos' : 'TIPOS',
    'var' : 'VARIABLES',
    'variables' : 'VARIABLES',
    'vector' : 'VECTOR',
}

# Lista de nombres de los tokens
tokens = ['PAREN_I', 'PAREN_D', 'LLAVE_I', 'LLAVE_D' , 'CORCH_I', 'CORCH_D',
          'S_MAS', 'S_MENOS', 'S_MULT', 'S_DIV', 'S_ASIGNACION', 
          'PUNTO', 'COMA', 'PUNTO_Y_COMA', 'DOS_PUNTOS', 'COMILLA_SIMPLE', 'COMILLA_DOBLE',
          'COMENTARIO', 'NUMERO', 'CADENA', 'ID'] + list(reserved.values())

# Reglas de expresiones regulares para tokens simples
t_PAREN_I = r'\('
t_PAREN_D = r'\)'
t_LLAVE_I = r'\{'
t_LLAVE_D = r'\}'
t_CORCH_I = r'\['
t_CORCH_D = r'\]'
t_S_MAS = r'\+'
t_S_MENOS = r'-'
t_S_MULT = r'\*'
t_S_DIV = r'/'
t_S_ASIGNACION = r'='
t_PUNTO = r'\.'
t_COMA = r','
t_PUNTO_Y_COMA = r';'
t_DOS_PUNTOS = r':'
t_COMILLA_SIMPLE = r'\''
t_COMILLA_DOBLE = r'\"'

def t_COMENTARIO(t):
    r'(/\*(.|\n)*?\*/)|(//.*)'
    pass

def t_NUMERO(t):
    r'[+-]?(\d+(\.\d+)?)([eE][+-]?\d+)?'
    try:
        t.value = float(t.value)    
    except ValueError:
        print "Linea %d: Numero %s es demasiado grande!" % (t.lineno, t.value)
        t.value = 0
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value,'ID')    # Verificar si es palabra reservada 
    return t

def t_CADENA(t):
    r'(\".*\")|(\'.*\')'
    return t

# Definimos esta regla para poder controlar los numeros de lineas 
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Una cadena que contiene caracteres a ignorar (espacios y tabuladores)
t_ignore  = ' \t'

# Regla para manejar errores
def t_error(t):
    print "Caracter ilegal: '%s'" % t.value[0]
    t.lexer.skip(1)

# Construimos el lexer
lex.lex()

if __name__ == '__main__':
    lex.runmain()
