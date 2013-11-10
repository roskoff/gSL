# -*- coding: utf-8 -*-

# Esta función retorna todas las funciones predeterminadas en SL, el
# conjunto de todas ellas sería nuestro RunTime Library (RTL)
def getFunctions():
    from ast import FunctionDef, For, Print, Name, Load, Store, arguments
    functions = []

    # imprimir(...)
    # Recibe cero o mas expresiones separadas por coma y las
    # imprme en pantalla separadas por un espacio
    #
    # Codigo Python
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
    return functions
