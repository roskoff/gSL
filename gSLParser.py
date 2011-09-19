# -*- coding: utf-8 -*-
#------------------------------------------------------------
# gSLParser.py
#
# Scanner para gSL
#------------------------------------------------------------
import inspect
from ast import *

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
    astree = Module( body = [])
    if len(p) == 4:
        # guardar ID del programa
        astree.body.append(Expr(value=Str(s=p[2])))
	# guardar las instrucciones del cuerpo
        if (p[3] != []):
            print_debug(p[3])
            astree.body = astree.body + p[3]

        print_debug("Nombre del programa: " + p[2])
	print_debug("Tabla de simbolos: " + str(identificadores))
    elif len (p) == 2:
	# guardar las instrucciones del cuerpo
        if (p[1] != []):
            astree.body = astree.body + p[1]

        print_debug("Nombre del programa: sin nombre definido")

    astree = fix_missing_locations(astree)
    p[0] = astree
    print_debug(dump(astree))

def p_body(p):
    """ body : declaration_list body_statements
             | declaration_list body_statements subrutine_list
    """
    # guardar las instrucciones del cuerpo
    p[0] = p[1] + p[2]
    if len(p) == 4:
        p[0] = p[0] + p[3]

def p_declaration_list(p):
    """ declaration_list : declaration_list declaration
                         | declaration
    """
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    if len(p) == 2:
        if p[1] == None or p[1] == []:
            p[0] = []
        else:
            p[0] = [p[1]]

def p_body_statements(p):
    """ body_statements : INICIO statement_list FIN
    """
    print_debug("Cuerpo principal")

    p[0] = p[2]

def p_statement_list(p):
    """ statement_list : statement_list statement
                       | statement
    """
    if len(p) == 2:
        print_debug("Instruccion: " + str(p[1]))

    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    if len(p) == 2:
        if p[1] == None or p[1] == []:
            p[0] = []
        else:
            p[0] = [p[1]]

def p_empty_statement(p):
    """ statement : empty
    """
    #p[0] = p[1] #"asf"

def p_subrutine_list(p):
    """ subrutine_list : subrutine_list subrutine
                       | subrutine
    """
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    if len(p) == 2:
        p[0] = [p[1]]

def p_subrutine(p):
    """ subrutine : subrutine_signature declaration_list body_statements
    """
    # Asignar al ambito secundario, registrar signature
    #p[0] = []

def p_subrutine_signature(p):
    """ subrutine_signature : function_signature
                            | procedure_signature
    """
    #p[0] = []

def p_function_signature(p):
    """ function_signature : SUBRUTINA IDENTIFICADOR PAREN_I parameters_list PAREN_D RETORNA IDENTIFICADOR
    """
    # XXX Recordar el manejo de la instruccion "retorna"
    # XXX Falta lista de parametros
    print_debug("Funcion creada: " + p[2])
    print_debug("Funcion retorna: " + p[6])
    #p[0] = []

def p_procedure_signature(p):
    """ procedure_signature : SUBRUTINA IDENTIFICADOR PAREN_I parameters_list PAREN_D
    """
    print_debug("Procedimiento creado: " + p[2])
    print_debug("Parametros: " + str(p[4]))
    # XXX Falta lista de parametros
    #p[0] = []

def p_parameters_list(p):
    """ parameters_list : parameters_list PUNTO_Y_COMA parameters_item
                        | parameters_item
    """
    #p[0] = []

def p_parameters_item(p):
    """ parameters_item : reference_optional variables_item
                        | empty
    """ 
    #p[0] = []

def p_reference_optional(p):
    """ reference_optional : REF
                           | empty
    """
    #p[0] = []

def p_declaration(p):
    """ declaration : VARIABLES variables_item_list
                    | TIPOS tipos_item_list
                    | CONSTANTES constantes_item_list
                    | empty
    """
    if len(p) == 3:
        print_debug("Declaracion: " + p[1])
    p[0] = p[1]

def p_variables_item_list(p):
    """ variables_item_list : variables_item_list variables_item
                            | variables_item
    """
    # Agregar a la tabla de simbolos, inicializar
    #p[0] = []

def p_variables_item(p):
    """ variables_item : id_list DOS_PUNTOS IDENTIFICADOR
    """
    print_debug("Tipo de la variable: (" + p[3] + ")")
    #p[0] = []

def p_tipos_item_list(p):
    """ tipos_item_list : tipos_item_list tipos_item
                        | tipos_item
    """
    #p[0] = []

def p_tipos_item(p):
    """ tipos_item : IDENTIFICADOR DOS_PUNTOS IDENTIFICADOR
    """
    print_debug("Tipo definido por usuario: (" + p[1] +":"+ p[3] + ")")
    #p[0] = []

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
    #p[0] = []


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
    #p[0] = []


def p_empty(p):
    """ empty :
    """
    #p[0] = []
    pass

def p_statement_assign(p):
    'statement : IDENTIFICADOR S_ASIGNACION expression'
    try:
        p[0] = identificadores[p[1]] # El ID debe estar previamente definido
        identificadores[p[1]] = p[3]
        print_debug(p[1] + ' <- ' + str(p[3]))
    except LookupError:
        print_debug("Identificador no está definido: '%s'" % p[1])
        p[0] = 0
    p[0] = Assign(targets=[Name(id=p[1], ctx=Store())], value=p[3])

def p_statement_subrutine_call(p):
    'statement : subrutine_call'
    p[0] = []

def p_subrutine_call(p):
    'subrutine_call : IDENTIFICADOR PAREN_I arguments_list PAREN_D'
    print_debug("Llamada a subrutina: " + p[1] + ", argumentos: " + str(p[3]))
    #p[0] = []

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
    #p[0] = p[1]

def p_expression_binop(p):
    '''expression : expression S_MAS expression
                  | expression S_MENOS expression
                  | expression S_MULT expression
                  | expression S_DIV expression'''
    if p[2] == '+'  : p[0] = BinOp(left=p[1], op=Add(), right=p[3])
    elif p[2] == '-': p[0] = BinOp(left=p[1], op=Sub(), right=p[3])
    elif p[2] == '*': p[0] = BinOp(left=p[1], op=Mult(), right=p[3])
    elif p[2] == '/': p[0] = BinOp(left=p[1], op=Div(), right=p[3])

def p_expression_uminus(p):
    'expression : S_MENOS expression %prec U_S_MENOS'
    p[0] = UnaryOp(op=USub(), operand=p[2])

def p_expression_uplus(p):
    'expression : S_MAS expression %prec U_S_MAS'
    p[0] = UnaryOp(op=UAdd(), operand=p[2])

def p_expression_group(p):
    'expression : PAREN_I expression PAREN_D'
    p[0] = p[2]

def p_expression_numero(p):
    'expression : NUMERO'
    p[0] = Num(n=p[1])

def p_expression_identificador(p):
    'expression : IDENTIFICADOR'
    try:
        p[0] = identificadores[p[1]]
    except LookupError:
        print("Identificador no está definido: '%s'" % p[1])
        p[0] = 0
    p[0] = Name(id=p[1], ctx=Load())

def p_expression_subrutine_call(p):
    "expression : subrutine_call"
    p[0] = -1 # XXX Por el momento se asigna -1 para ver el efecto que tien en las expresiones

def p_error(t):
    print("Syntax error at '%s'" % t.value)

from gSLLexer import gSLLexer, tokens
import ply.yacc as yacc
gLexer = gSLLexer()
yacc.yacc()
