import ply.yacc as yacc
import inspect

# Get the token map from the lexer.  This is required.
from lex import tokens

DEBUG = True

# Funciones utilitarias
def print_debug(mensaje):
    # Para saber el nombre de la funcion en la que estamos
    function_name = inspect.stack()[1][3]
    if DEBUG: print "gSL DEBUG >> Funcion: ", function_name, ">" , mensaje

def p_start(p):
    """ start : PROGRAMA ID body
              | body
    """
    if len(p) == 4:
        # guardar ID del programa
        p[0] = p[3] 
	print_debug("Nombre del programa: " + p[2])
    elif len (p) == 2:
        p[0] == p[1]
	print_debug("Nombre del programa: sin nombre definido")

def p_body(p):
    """ body : declaration_list body_statements
             | declaration_list body_statements subrutine_list
    """
    # Declarar variables
    p[0] = [p[1], p[2]]
 
def p_declaration_list(p):
    """ declaration_list : declaration_list declaration
                         | declaration
    """
    if len(p) == 3:
        p[0] = [p[2]] + p[1]
    elif len(p) == 2:
        p[0] = [p[1]]

def p_declaration(p):
    """ declaration : VARIABLES variables_item_list
                    | TIPOS tipos_item_list
                    | CONSTANTES constantes_item_list
    """
    p[0] = p[2]

def p_variables_item_list(p):
    """ variables_item_list : variables_item_list variables_item
                            | variables_item
    """
    # Agregar a la tabla de simbolos, inicializar

def p_variables_item(p):
    """ variables_item : id_list DOS_PUNTOS ID 
    """
    print_debug("Tipo de la variable: (" + p[3] + ")")

def p_tipos_item_list(p):
    """ tipos_item_list : tipos_item_list ID DOS_PUNTOS ID 
                        | tipos_item
    """
    # Agregar a la tabla de simbolos

def p_tipos_item(p):
    """ tipos_item : ID DOS_PUNTOS ID 
    """
    print_debug("Tipo definido por usuario: (" + p[3] + ")")

def p_constantes_item_list(p):
    """ constantes_item_list : constantes_item_list ID S_ASIGNACION ID 
                             | constantes_item
    """
    # Agregar a la tabla de simbolos, inicializar

def p_constantes_item(p):
    """ constantes_item : ID S_ASIGNACION ID 
                        | ID S_ASIGNACION NUMERO
                        | ID S_ASIGNACION CADENA
    """
    print_debug("Constante definida por usuario: (" + str(p[3]) + ")")

def p_id_list(p):
    """ id_list : id_list COMA ID
                | ID
    """
    if len(p) == 4:
        p[0] = [p[3]] + p[1]
    elif len(p) == 2:
        p[0] = [p[1]]
    print_debug( "Lista IDs: (" + str(p[0]) + ")")


def p_subrutine_list(p):
    """ subrutine_list : subrutine_list subrutine
                       | subrutine
    """
    if len(p) == 3:
        p[0] = [p[2]] + p[1]
    elif len(p) == 2:
        p[0] = [p[1]]

def p_subrutine(p):
    """ subrutine : subrutine_signature declaration_list body_statements
    """
    # Asignar al ambito secundario, registrar signature

def p_subrutine_signature(p):
    """ subrutine_signature : function_signature
                            | procedure_signature
    """

def p_function_signature(p):
    """ function_signature : SUBRUTINA ID PAREN_I PAREN_D RETORNA ID
    """
    # XXX Recordar el manejo de la instruccion "retorna"
    # XXX Falta lista de parametros
    print_debug("Funcion creada: " + p[2])
    print_debug("Funcion retorna: " + p[6])

def p_procedure_signature(p):
    """ procedure_signature : SUBRUTINA ID PAREN_I PAREN_D
    """
    print_debug("Procedimiento creado: " + p[2])
    # XXX Falta lista de parametros

def p_body_statements(p):
    """ body_statements : INICIO statement_list FIN
    """
    p[0] = p[1]

def p_statement_list(p):
    """ statement_list : empty
    """
    p[0] = p[1]

def p_empty(p):
    """ empty :
    """
    pass

yacc.yacc() 


