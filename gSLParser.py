# -*- coding: utf-8 -*-
#------------------------------------------------------------
# gSLParser.py
#
# Scanner para gSL
#------------------------------------------------------------
import inspect
from ast import *

def gSLParser(debug):
    DEBUG = debug

    # Funciones utilitarias
    def print_debug(mensaje):
        # Para saber el nombre de la funcion en la que estamos
        function_name = inspect.stack()[1][3]
        if DEBUG: print "gSL DEBUG >> Funcion: ", function_name, ">" , mensaje

    # Establecemos las precedencias y asociatividad
    precedence = (
        ('left','OR'),
        ('left','AND'),
        ('right','NOT'),
        ('left','S_MENOR_QUE', 'S_MAYOR_QUE', 'S_MENOR_IGUAL_QUE', 'S_MAYOR_IGUAL_QUE', 'S_IGUAL_QUE', 'S_DISTINTO_DE'),
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
        # Antes que nada se agregan los tipos de datos predefinidos
        tipos_predefinidos = [
            Assign(targets = [Name(id = 'cadena', ctx = Store())], value = Str(s = '')),
            Assign(targets = [Name(id = 'numerico', ctx = Store())], value = Num(n = 0)),
            Assign(targets = [Name(id = 'logico', ctx = Store())], value = Name( id = 'True', ctx = Load()))
            ]
        astree.body = astree.body + tipos_predefinidos

        if len(p) == 4:
            program_id = p[2]
            program_body = p[3]

        elif len (p) == 2:
            program_id = 'sin nombre' 
            program_body = p[1]

        # guardar ID del programa
        astree.body.append(
            Expr(value = Str(s = program_id) )
        )
        # guardar las instrucciones del cuerpo
        if (program_body != []):
            astree.body = astree.body + program_body


        astree = fix_missing_locations(astree)
        p[0] = astree

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
            if p[2] == None or p[2] == []:
                p[0] = p[1]
            else:
                p[0] = p[1] + p[2]
        if len(p) == 2:
            if p[1] == None or p[1] == []:
                p[0] = []
            else:
                p[0] = p[1]

    def p_body_statements(p):
        """ body_statements : INICIO statement_list FIN
        """
        p[0] = p[2]

    def p_statement_list_compund(p):
        """ statement_list : statement_list multiple_statement
        """
        #""" statement_list : statement_list statement
        #                   | statement
        # p_statement_list se separa en 2 (compound y simple) para
        # simplificar la funcion

        # Si multiple_statement resulta una lista, concatenar listas,
        # si es un nodo, agregarlo como elemento.
        if isinstance(p[2], list):
            p[0] = p[1] + p[2]
        else:
            p[0] = p[1] + [p[2]]

    def p_statement_list_simple(p):
        """ statement_list : multiple_statement
        """
        # p_statement_list se separa en 2 (compound y simple) para
        # simplificar la funcion

        # Si multiple_statement resulta una lista, concatenar listas,
        # si es un nodo, agregarlo como elemento.
        if p[1] == None or p[1] == []:
            p[0] = []
        else:
            if isinstance(p[1], list):
                p[0] = p[1]
            else:
                p[0] = [p[1]]

    def p_empty_statement(p):
        """ statement : empty
        """
        #p[0] = p[1] #"asf"

    def p_multiple_statement(p):
        """ multiple_statement : multiple_statement PUNTO_Y_COMA statement
                               | statement
        """
        if len(p) == 4:
            p[0] = p[1] + [p[3]]
        elif len(p) == 2:
            p[0] = [p[1]]

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
            p[0] = p[2]

    def p_variables_item_list(p):
        """ variables_item_list : variables_item_list variables_item
                                | variables_item
        """
        # Agregar a la tabla de simbolos, inicializar
        if len(p) == 3:
            p[0] = p[1] + [p[2]]
        if len(p) == 2:
            p[0] = [p[1]]

    def p_variables_item(p):
        """ variables_item : id_list DOS_PUNTOS IDENTIFICADOR
        """
        print_debug("Tipo de la variable: (" + p[3] + ")")
        #XXX Controlar que IDENTIFICADOR sea un tipo de dato
        id_list = []
        for var_id in p[1]:
            id_list.append(
                Name(id = var_id,
                     ctx = Store())
            )
        p[0] = Assign(targets = id_list,
                      value = Name(id = p[3],
                                   ctx = Load())
                     )

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
            print_debug("'%s' no está definido'" % p[1])
            raise NameError("'%s' no está definido" % p[1])

        p[0] = Assign(targets = [Name(id=p[1], ctx=Store())],
                      value = p[3])

    def p_statement_if(p):
        'statement : SI PAREN_I bool_expression PAREN_D LLAVE_I statement_list LLAVE_D'
        p[0] = If(test = p[3], body = p[6], orelse = [])
        print_debug("SI: (" + str(p[3]) +")")

    def p_statement_if_else(p):
        'statement : SI PAREN_I bool_expression PAREN_D LLAVE_I statement_list SINO statement_list LLAVE_D'
        p[0] = If(test = p[3], body = p[6], orelse = p[8])

    def p_statement_subrutine_call(p):
        'statement : subrutine_call'
        p[0] = p[1]

    def p_subrutine_call(p):
        'subrutine_call : IDENTIFICADOR PAREN_I arguments_list PAREN_D'
        print_debug("Llamada a subrutina: " + p[1] + ", argumentos: " + str(p[3]))
        # Si no se reciben argumentos, pasar lista vacía
        if p[3] == [None]: p[3] = []
        p[0] = Expr(value = Call(func = Name(id = p[1], ctx=Load()),
                                 args = p[3],
                                 keywords=[],
                                 starargs=None, kwargs=None))
        print_debug(dump(p[0]))
    
    def p_arguments_list(p):
        """arguments_list : arguments_list COMA argument
                          | argument
        """
        if len(p) == 4:
            p[0] = p[1] + [p[3]]
        elif len(p) == 2:
            p[0] = [p[1]]
    
    def p_argument(p):
        """ argument : expression
                     | empty
        """
        p[0] = p[1]

    def p_expression_bool(p):
        '''bool_expression : bool_expression OR bool_expression
                           | and_expression'''
        if len(p) == 2:
            p[0] = p[1]
            print_debug("bool_expression: (" + str(p[0]) +")")
        elif len(p) == 4:
            p[0] = BoolOp(op = Or(), values = [p[1], p[3]])

    def p_expression_and(p):
        '''and_expression : and_expression AND and_expression
                          | NOT and_expression
                          | test_expression'''
        if len(p) == 4:
            p[0] = BoolOp(op = And(), values = [p[1], p[3]])
        elif len(p) == 3:
            p[0] = UnaryOp(op = Not(), operand = p[2])
        elif len(p) == 2:
            p[0] = p[1]
            print_debug("and_expression: (" + str(p[1]) +")")

    def p_expression_comp(p):
        '''test_expression : expression S_MENOR_QUE expression
                           | expression S_MAYOR_QUE expression
                           | expression S_MENOR_IGUAL_QUE expression
                           | expression S_MAYOR_IGUAL_QUE expression
                           | expression S_IGUAL_QUE expression
                           | expression S_DISTINTO_DE expression'''
        if   p[2] == '<' : p[0] = Compare(left = p[1], ops = [Lt()], comparators = [p[3]])
        elif p[2] == '>' : p[0] = Compare(left = p[1], ops = [Gt()], comparators = [p[3]])
        elif p[2] == '<=': p[0] = Compare(left = p[1], ops = [LtE()], comparators = [p[3]])
        elif p[2] == '>=': p[0] = Compare(left = p[1], ops = [GtE()], comparators = [p[3]])
        elif p[2] == '==': p[0] = Compare(left = p[1], ops = [Eq()], comparators = [p[3]])
        elif p[2] == '<>': p[0] = Compare(left = p[1], ops = [NotEq()], comparators = [p[3]])

    def p_expression_test_exp_group(p):
        '''test_expression : PAREN_I bool_expression PAREN_D'''
        p[0] = p[2]

    def p_expression_binop(p):
        '''expression : expression S_MAS expression
                      | expression S_MENOS expression
                      | expression S_MULT expression
                      | expression S_DIV expression'''
        if   p[2] == '+': p[0] = BinOp(left = p[1], op = Add(),  right = p[3])
        elif p[2] == '-': p[0] = BinOp(left = p[1], op = Sub(),  right = p[3])
        elif p[2] == '*': p[0] = BinOp(left = p[1], op = Mult(), right = p[3])
        elif p[2] == '/': p[0] = BinOp(left = p[1], op = Div(),  right = p[3])

    def p_expression_uminus(p):
        'expression : S_MENOS expression %prec U_S_MENOS'
        p[0] = UnaryOp(op = USub(), operand = p[2])

    def p_expression_uplus(p):
        'expression : S_MAS expression %prec U_S_MAS'
        p[0] = UnaryOp(op = UAdd(), operand = p[2])

    def p_expression_group(p):
        'expression : PAREN_I expression PAREN_D'
        p[0] = p[2]

    def p_expression_numero(p):
        'expression : NUMERO'
        p[0] = Num(n = p[1])

    def p_expression_identificador(p):
        'expression : IDENTIFICADOR'
        try:
            p[0] = identificadores[p[1]]
        except LookupError:
            print("Identificador no está definido: '%s'" % p[1])
            p[0] = 0
        p[0] = Name(id = p[1],
                    ctx=Load())

    def p_expression_cadena(p):
        'expression : CADENA'
        # Tomamos desde el segundo caracter hasta el penúltimo
        # para sacar las comillas
        p[0] = Str(s = p[1][1:-1])
        print_debug("Cadena: '%s'" % p[1])

    def p_expression_subrutine_call(p):
        "expression : subrutine_call"
        p[0] = -1 # XXX Por el momento se asigna -1 para ver el efecto que tien en las expresiones

    def p_error(t):
        print("Syntax error at '%s'" % t.value)

    # Build and return the parser
    from gSLLexer import gSLLexer, tokens
    import ply.yacc as yacc
    gLexer = gSLLexer()
    return yacc.yacc()
