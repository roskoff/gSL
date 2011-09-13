# -*- coding: utf-8 -*-
#------------------------------------------------------------
# gSLParser.py
#
# Scanner para gSL
#------------------------------------------------------------
import inspect

DEBUG = True

# Funciones utilitarias
def print_debug(mensaje):
    # Para saber el nombre de la funcion en la que estamos
    function_name = inspect.stack()[1][3]
    if DEBUG: print "gSL DEBUG >> Funcion: ", function_name, ">" , mensaje

# Establecemos las precedencias y asociatividad
precedence = (
    ('left','S_MAS','S_MENOS'),
    ('left','S_MULT','S_DIV'),
    ('right','U_S_MENOS','U_S_MAS'),
    )

# Diccionario que contiene los identificadores que vamos encontrando
identificadores = { }

def p_start(p):
    """ start : PROGRAMA IDENTIFICADOR body
              | body
    """
    if len(p) == 4:
        # guardar ID del programa
        print_debug("Nombre del programa: " + p[2])
	print_debug("Tabla de simbolos: " + str(identificadores))
    elif len (p) == 2:
        print_debug("Nombre del programa: sin nombre definido")

def p_body(p):
    """ body : declaration_list body_statements
             | declaration_list body_statements subrutine_list
    """

def p_declaration_list(p):
    """ declaration_list : declaration_list declaration
                         | declaration
    """

def p_body_statements(p):
    """ body_statements : INICIO statement_list FIN
    """
    print_debug("Cuerpo principal")

def p_statement_list(p):
    """ statement_list : statement_list statement
                       | statement
		       | empty
    """
    if len(p) == 2:
        print_debug("Instruccion: " + str(p[1]))

def p_subrutine_list(p):
    """ subrutine_list : subrutine_list subrutine
                       | subrutine
    """

def p_subrutine(p):
    """ subrutine : subrutine_signature declaration_list body_statements
    """
    # Asignar al ambito secundario, registrar signature

def p_subrutine_signature(p):
    """ subrutine_signature : function_signature
                            | procedure_signature
    """

def p_function_signature(p):
    """ function_signature : SUBRUTINA IDENTIFICADOR PAREN_I parameters_list PAREN_D RETORNA IDENTIFICADOR
    """
    # XXX Recordar el manejo de la instruccion "retorna"
    # XXX Falta lista de parametros
    print_debug("Funcion creada: " + p[2])
    print_debug("Funcion retorna: " + p[6])

def p_procedure_signature(p):
    """ procedure_signature : SUBRUTINA IDENTIFICADOR PAREN_I parameters_list PAREN_D
    """
    print_debug("Procedimiento creado: " + p[2])
    print_debug("Parametros: " + str(p[4]))
    # XXX Falta lista de parametros

def p_parameters_list(p):
    """ parameters_list : parameters_list PUNTO_Y_COMA parameters_item
                        | parameters_item
    """

def p_parameters_item(p):
    """ parameters_item : reference_optional variables_item
                        | empty
    """ 
def p_reference_optional(p):
    """ reference_optional : REF
                           | empty
    """

def p_declaration(p):
    """ declaration : VARIABLES variables_item_list
                    | TIPOS tipos_item_list
                    | CONSTANTES constantes_item_list
                    | empty
    """
    if len(p) == 3:
        print_debug("Declaracion: " + p[1])

def p_variables_item_list(p):
    """ variables_item_list : variables_item_list variables_item
                            | variables_item
    """
    # Agregar a la tabla de simbolos, inicializar

def p_variables_item(p):
    """ variables_item : id_list DOS_PUNTOS IDENTIFICADOR
    """
    print_debug("Tipo de la variable: (" + p[3] + ")")

def p_tipos_item_list(p):
    """ tipos_item_list : tipos_item_list tipos_item
                        | tipos_item
    """

def p_tipos_item(p):
    """ tipos_item : IDENTIFICADOR DOS_PUNTOS IDENTIFICADOR
    """
    print_debug("Tipo definido por usuario: (" + p[1] +":"+ p[3] + ")")

def p_constantes_item_list(p):
    """ constantes_item_list : constantes_item_list constantes_item
                             | constantes_item
    """
    # Agregar a la tabla de simbolos, inicializar

def p_constantes_item(p):
    """ constantes_item : IDENTIFICADOR S_ASIGNACION IDENTIFICADOR 
                        | IDENTIFICADOR S_ASIGNACION NUMERO
                        | IDENTIFICADOR S_ASIGNACION CADENA
    """
    # XXX El segundo IDENTIFICADOR en la primera produccion debe ser
    # necesariamente otra constante (incluyendo constantes predefinidas
    # tales como TRUE y FALSE
    print_debug("Constante definida por usuario: (" + str(p[1]) +":"+ str(p[3]) + ")")


def p_id_list(p):
    """ id_list : id_list COMA IDENTIFICADOR
                | IDENTIFICADOR
    """
    if len(p) == 4:
        p[0] = [p[3]] + p[1]
    elif len(p) == 2:
        p[0] = [p[1]]
        identificadores[p[1]] = 0 # Define e inicializa
    print_debug( "Lista IDs: (" + str(p[0]) + ")")


def p_empty(p):
    """ empty :
    """
    pass

def p_statement_assign(t):
    'statement : IDENTIFICADOR S_ASIGNACION expression'
    try:
        t[0] = identificadores[t[1]] # El ID debe estar previamente definido
        identificadores[t[1]] = t[3]
        print(t[1] + ' <- ' + str(t[3]))
    except LookupError:
        print("Identificador no está definido: '%s'" % t[1])
        t[0] = 0

def p_statement_subrutine_call(p):
    'statement : subrutine_call'

def p_subrutine_call(p):
    'subrutine_call : IDENTIFICADOR PAREN_I arguments_list PAREN_D'
    print_debug("Llamada a subrutina: " + p[1] + ", argumentos: " + str(p[3]))

def p_arguments_list(p):
    """arguments_list : arguments_list COMA argument
                      | argument
    """
    if len(p) == 4:
        p[0] = [p[3]] + p[1]
    elif len(p) == 2:
        p[0] = [p[1]]

def p_argument(p):
    """ argument : expression
                 | empty
    """
    p[0] = p[1]

def p_expression_binop(t):
    '''expression : expression S_MAS expression
                  | expression S_MENOS expression
                  | expression S_MULT expression
                  | expression S_DIV expression'''
    if t[2] == '+'  : t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]

def p_expression_uminus(t):
    'expression : S_MENOS expression %prec U_S_MENOS'
    t[0] = -t[2]

def p_expression_uplus(t):
    'expression : S_MAS expression %prec U_S_MAS'
    t[0] = +t[2]

def p_expression_group(t):
    'expression : PAREN_I expression PAREN_D'
    t[0] = t[2]

def p_expression_numero(t):
    'expression : NUMERO'
    t[0] = t[1]

def p_expression_identificador(t):
    'expression : IDENTIFICADOR'
    try:
        t[0] = identificadores[t[1]]
    except LookupError:
        print("Identificador no está definido: '%s'" % t[1])
        t[0] = 0

def p_expression_subrutine_call(p):
    "expression : subrutine_call"
    p[0] = -1 # XXX Por el momento se asigna -1 para ver el efecto que tien en las expresiones

def p_error(t):
    print("Syntax error at '%s'" % t.value)

from gSLLexer import gSLLexer, tokens
import ply.yacc as yacc
gLexer = gSLLexer()
yacc.yacc()
