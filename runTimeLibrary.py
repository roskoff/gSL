# -*- coding: utf-8 -*-

# Esta función retorna todas las funciones predeterminadas en SL, el
# conjunto de todas ellas sería nuestro RunTime Library (RTL)
def getFunctions():
    from ast import FunctionDef, For, Print, Name, Load, Store, Assign, Call, Attribute, arguments
    from ast import Str, If, Compare, NotEq, Raise, Num, While
    from ast import Lt, Subscript, Add, Index, AugAssign, ListComp, comprehension
    functions = []

    # imprimir(...)
    # Recibe cero o mas expresiones separadas por coma y las
    # imprime en pantalla separadas por un espacio
    #
    # Código Python
    # def imprimir(*args):
    #     for arg in args:
    #         print arg,
    #     print
    #
    functions.append(FunctionDef(name = 'imprimir',
                                args = arguments(args   = [],
                                                 vararg = 'args',
                                                 kwarg  = None,
                                                 defaults = []),
                                body = [For(target = Name(id = 'arg', ctx=Store()),
                                            iter   = Name(id = 'args', ctx=Load()),
                                            body   = [Print(dest = None, values = [Name(id = 'arg', ctx=Load())], nl=False)],
                                            orelse=[]),
                                        Print(dest=None, values=[], nl=True)],
                                decorator_list=[]))
    # leer(...)
    # Lee uno o mas valores y los asigna a las variables que
    # se pasan como parámetros
    #
    # Código Python
#def leer(*args):
#    input_values = raw_input()
#    list_values = input_values.split(',')
#    args_list = [arg for arg in args]
#    count_values = len(list_values)
#    if len(args) != count_values:
#        raise Exception("Error de ejecución, ya no hay datos de entrada para la función leer()")
#    i = 0
#    while (i < count_values):
#        args_list[i] = list_values[i]
#        i += 1

    functions.append(FunctionDef(name = 'leer',
                                args = arguments(args   = [],
                                                 vararg = 'args',
                                                 kwarg  = None,
                                                 defaults = []),
                                body = [Assign(targets = [Name(id = 'input_values', ctx=Store())],
                                               value   = Call(func = Name(id = 'raw_input', ctx=Load()),
                                                              args = [],
                                                              keywords = [],
                                                              starargs = None,
                                                              kwargs   = None)),
                                        Assign(targets = [Name(id = 'list_values', ctx=Store())],
                                               value   = Call(func = Attribute(value = Name(id = 'input_values', ctx=Load()),
                                                              attr = 'split', ctx=Load()),
                                                              args = [Str(s = ',')],
                                                              keywords = [],
                                                              starargs = None,
                                                              kwargs   = None)),
                                        Assign(targets = [Name(id = 'args_list', ctx=Store())],
                                               value   = ListComp(elt = Name(id = 'arg', ctx=Load()),
                                                                  generators = [comprehension(target = Name(id = 'arg', ctx=Store()),
                                                                                              iter = Name(id = 'args', ctx=Load()),
                                                                                              ifs=[])])),
                                        Assign(targets = [Name(id = 'count_values', ctx=Store())],
                                               value   = Call(func = Name(id = 'len', ctx=Load()),
                                                              args = [Name(id = 'list_values', ctx=Load())],
                                                              keywords = [],
                                                              starargs = None,
                                                              kwargs = None)),
                                        If(test = Compare(left = Call(func = Name(id = 'len', ctx=Load()),
                                                                      args = [Name(id = 'args', ctx=Load())],
                                                                      keywords = [],
                                                                      starargs = None,
                                                                      kwargs   = None),
                                                          ops = [NotEq()],
                                                          comparators = [Name(id = 'count_values', ctx=Load())]),
                                           body=[Raise(type = Call(func = Name(id = 'Exception', ctx=Load()),
                                                                   args = [Str(s = 'Error de ejecuci\\xc3\\xb3n, ya no hay datos de entrada para la funci\\xc3\\xb3n leer()')],
                                                                   keywords = [],
                                                                   starargs = None,
                                                                   kwargs   = None),
                                                       inst = None,
                                                       tback = None)],
                                           orelse=[]),
                                        Assign(targets = [Name(id = 'i', ctx=Store())],
                                               value   = Num(n = 0)),
                                        While(test = Compare(left = Name(id = 'i', ctx=Load()),
                                                             ops = [Lt()],
                                                             comparators = [Name(id = 'count_values', ctx=Load())]),
                                              body=[Assign(targets = [Subscript(value = Name(id = 'args_list', ctx=Load()),
                                                                                slice = Index(value = Name(id = 'i', ctx=Load())),
                                                                                ctx=Store())],
                                                           value = Subscript(value = Name(id = 'list_values', ctx=Load()),
                                                                             slice = Index(value = Name(id = 'i', ctx=Load())),
                                                                             ctx=Load())),
                                                    AugAssign(target = Name(id = 'i', ctx=Store()), op = Add(), value = Num(n = 1))],
                                              orelse=[])],
                                decorator_list=[]))

    return functions
